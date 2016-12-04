#!/
# Modified from https://groups.google.com/d/msg/youtube8m-users/yEDzH7EqUf8/EfW0WO3jAgAJ
import sys
import tensorflow as tf
import numpy as np
from tensorflow.python.platform import gfile
import codecs, json
import base64
import pandas as pd


def Dequantize(feat_vector, max_quantized_value=2, min_quantized_value=-2):
  """Dequantize the feature from the byte format to the float format.

  Args:
    feat_vector: the input 1-d vector.
    max_quantized_value: the maximum of the quantized value.
    min_quantized_value: the minimum of the quantized value.

  Returns:
    A float vector which has the same shape as feat_vector.
  """
  assert max_quantized_value >  min_quantized_value
  quantized_range = max_quantized_value - min_quantized_value
  scalar = quantized_range / 255.0
  bias = (quantized_range / 512.0) + min_quantized_value
  return feat_vector * scalar + bias


class YouTube8MFrameFeatureReader:
  def __init__(self,
               num_classes=4800,
               feature_size=1024,
               feature_name="inc3",
               max_frames=300,
               sequence_data=True):
    self.num_classes = num_classes
    self.feature_size = feature_size
    self.feature_name = feature_name
    self.max_frames = max_frames
    self.sequence_data = sequence_data

  def prepare_reader(self,
                     filename_queue,
                     max_quantized_value=2,
                     min_quantized_value=-2):
    reader = tf.TFRecordReader()
    _, serialized_example = reader.read(filename_queue)

    context_features, sequence_features = {
        "video_id": tf.FixedLenFeature([], tf.string),
        "labels": tf.VarLenFeature(tf.int64),
    }, None
    if self.sequence_data:
      sequence_features = {
          self.feature_name: tf.FixedLenSequenceFeature([], dtype=tf.string),
      }
    else:
      context_features[self.feature_name] = tf.FixedLenFeature(self.feature_size, tf.float32)

    contexts, features = tf.parse_single_sequence_example(
        serialized_example,
        context_features=context_features,
        sequence_features=sequence_features)

    labels = (tf.cast(
        tf.sparse_to_dense(contexts["labels"].values, (self.num_classes,), 1),
        tf.bool))

    if self.sequence_data:
      decoded_features = tf.reshape(
          tf.cast(
              tf.decode_raw(features[self.feature_name], tf.uint8), tf.float32),
          [-1, self.feature_size])
      num_frames = tf.minimum(tf.shape(decoded_features)[0], self.max_frames)
      video_matrix = Dequantize(decoded_features, max_quantized_value,
                                min_quantized_value)
    else:
      video_matrix = contexts[self.feature_name]
      num_frames = tf.constant(-1)

    # Pad or truncate to 'max_frames' frames.
    # video_matrix = resize_axis(video_matrix, 0, self.max_frames)
    return contexts["video_id"], video_matrix, labels, num_frames

def main(level, files_pattern, outpath):
  labelshisto=pd.read_csv("train-labels-histogram.csv")
  alllabels=labelshisto["LabelName"].values
  data_files = gfile.Glob(files_pattern)
  filename_queue = tf.train.string_input_producer(
      data_files, num_epochs=1, shuffle=False)

  if level == 'frame':
    reader = YouTube8MFrameFeatureReader(feature_name="inc3")
  elif level == 'video':
    reader = YouTube8MFrameFeatureReader(feature_name="mean_inc3", sequence_data=False)
  vals = reader.prepare_reader(filename_queue)

  with tf.Session() as sess:
    sess.run(tf.initialize_local_variables())
    sess.run(tf.initialize_all_variables())
    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(sess=sess, coord=coord)
    f=codecs.open(outpath, "w" , encoding='utf-8')
    fa=codecs.open(outpath, "a", encoding='utf-8')
    try:
      counter=0
      recordlist=[]
      while not coord.should_stop():
        counter+=1
        vid, features, labels, _ = sess.run(vals)
        #features=base64.b64encode(np.round(features, decimals=5))
        #labels=base64.b64encode(labels)
        featureslist=np.round(features,decimals=5).tolist()
        labelName=alllabels[np.where(labels)[0][0]]
        record={"vid":vid, "features": str(featureslist), "labels":labelName}
        '''
        Option 1: write each record on a line
        if counter==1:
            f.write("{}\n".format(json.dumps(record)))
        else:
            fa.write("{}\n".format(json.dumps(record)))
        '''
        '''
        Option 2: put all objects in an array and output everything at once
        '''
        recordlist.append(record)
    except tf.errors.OutOfRangeError:
      print('Finished extracting.')
    finally:
      json.dump(recordlist, f, separators=(',', ':'))
      coord.request_stop()
      coord.join(threads)
      f.close()


if __name__ == '__main__':
  '''
  level: 'frame' or 'video'
  files_pattern: "train*.tfrecord"
  '''
  level, files_pattern, output= sys.argv[1: ]
  main(level, files_pattern, output)
