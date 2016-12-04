import tensorflow as tf
from tensorflow.python.ops import parsing_ops
from tensorflow.contrib.slim.python.slim.data import parallel_reader
import numpy as np


def main():
  reader = tf.TFRecordReader
  data_sources = ["traineh.tfrecord"]
  _, data = parallel_reader.parallel_read(
      data_sources,
      reader_class=reader,
      num_epochs=1,
      num_readers=1,
      shuffle=False,
      capacity=256,
      min_after_dequeue=1)

  context_features, sequence_features = parsing_ops.parse_single_sequence_example(data, context_features={
      'video_id': tf.VarLenFeature(tf.string),
      'labels': tf.VarLenFeature(tf.int64),
    }, sequence_features={
      'inc3': tf.FixedLenSequenceFeature(1, tf.string)
    }, example_name="")

  with tf.Session() as sess:
    sess.run(tf.initialize_local_variables())
    sess.run(tf.initialize_all_variables())
    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(sess=sess, coord=coord)

    try:
      while not coord.should_stop():
        meta = sess.run(context_features)
        vid = meta['video_id'].values[0]
        labels = meta['labels'].values

        inc3_fea = sess.run(sequence_features)['inc3']
        frame_feas = []
        for r in inc3_fea:
          v = np.fromstring(r[0], dtype=np.uint8)
          frame_feas.append(v[None, :])
        frame_feas = np.vstack(frame_feas)
        print(vid, labels)
        print(frame_feas.shape)
        # Do something here
    except tf.errors.OutOfRangeError:
      print('Finished extracting.')
    finally:
      coord.request_stop()
      coord.join(threads)



if __name__ == '__main__':
  main()
