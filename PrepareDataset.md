# Download/parse the dataset
## 1. Download the video level

```
$ mkdir yt8m_video_level
$ cd yt8m_video_level/
$ curl us.data.yt8m.org/0/video_level/train/download.py | python
```
shell output:

```
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  2181  100  2181    0     0   1136      0  0:00:01  0:00:01 --:--:--  5894
/Users/Doran/anaconda2/bin/curl
Starting fresh download in this directory. Please make sure you have >2TB of free disk space!
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  224k  100  224k    0     0    98k      0  0:00:02  0:00:02 --:--:--   99k
Files remaining 4096
Downloading: traineh.tfrecord
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 5578k  100 5578k    0     0  2050k      0  0:00:02  0:00:02 --:--:-- 2051k
Successfully downloaded traineh.tfrecord


Downloading: trainKH.tfrecord
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 5639k  100 5639k    0     0  1057k      0  0:00:05  0:00:05 --:--:-- 1364k
Successfully downloaded trainKH.tfrecord
```

## 2. Parse dataset
Use code from google group: https://groups.google.com/d/msg/youtube8m-users/yEDzH7EqUf8/EfW0WO3jAgAJ

```
python yt8m_parse.py video /PATH/TO/YOUR/VIDEO/LEVEL/DIR/*.tfrecord
python yt8m_parse.py frame /PATH/TO/YOUR/FRAME/LEVEL/DIR/*.tfrecord
```

My changes: 
I ran the above code in jupyter notebook. To execute use this instead:

```
main('video', '/Users/Doran/Desktop/yt8m_video_level/train*.tfrecord')
```

Output:
I have no idea what this means.. I've asked the script author if he can explain this to me. 
I also get an error in the middle so I don't know what the end result looks like. I'am planning to debug it over the weekend.

```
('_1fwf2v5Ly4', array([-0.26583609, -0.03337166,  1.77707052, ..., -0.21188761,
        0.66285288, -0.42780456], dtype=float32), array([False, False, False, ..., False, False, False], dtype=bool))
('_1!', array([ 0.33659682, -0.66403061, -0.55846202, ...,  0.10260989,
       -0.53587377,  0.21952492], dtype=float32), array([False, False, False, ..., False, False, False], dtype=bool))
('_1bksg3puEo', array([ 0.46828187, -1.29963446, -0.15900657, ..., -0.15803124,
        0.43130127, -0.29741964], dtype=float32), array([False, False, False, ..., False, False, False], dtype=bool))
('_1kknY0KpPM', array([-1.07382739,  0.82021892,  0.93392062, ..., -0.3786878 ,
        0.22442569,  0.08657661], dtype=float32), array([False, False, False, ..., False, False, False], dtype=bool))
('_14Y-JJ5Kcg', array([ 0.01543701, -1.17169154,  0.13983409, ..., -0.05419474,
       -0.12896416,  0.10851619], dtype=float32), array([False, False, False, ..., False, False, False], dtype=bool))

---------------------------------------------------------------------------
KeyboardInterrupt                         Traceback (most recent call last)
<ipython-input-4-4d5564c8ea3b> in <module>()
----> 1 main('video', '/Users/Doran/Desktop/yt8m_video_level/train*.tfrecord')

<ipython-input-3-1a59a01d431c> in main(level, files_pattern)
     99       while not coord.should_stop():
    100         vid, features, labels, _ = sess.run(vals)
--> 101         print(vid, features, labels)
    102     except tf.errors.OutOfRangeError:
    103       print('Finished extracting.')

/Users/Doran/anaconda2/lib/python2.7/site-packages/numpy/core/numeric.pyc in array_repr(arr, max_line_width, precision, suppress_small)
   1805     if arr.size > 0 or arr.shape == (0,):
   1806         lst = array2string(arr, max_line_width, precision, suppress_small,
-> 1807                            ', ', "array(")
   1808     else:  # show zero-length shape unless it is (0,)
   1809         lst = "[], shape=%s" % (repr(arr.shape),)

/Users/Doran/anaconda2/lib/python2.7/site-packages/numpy/core/arrayprint.pyc in array2string(a, max_line_width, precision, suppress_small, separator, prefix, style, formatter)
    445     else:
    446         lst = _array2string(a, max_line_width, precision, suppress_small,
--> 447                             separator, prefix, formatter=formatter)
    448     return lst
    449 

/Users/Doran/anaconda2/lib/python2.7/site-packages/numpy/core/arrayprint.pyc in _array2string(a, max_line_width, precision, suppress_small, separator, prefix, formatter)
    258 
    259     formatdict = {'bool': _boolFormatter,
--> 260                   'int': IntegerFormat(data),
    261                   'float': FloatFormat(data, precision, suppress_small),
    262                   'longfloat': LongFloatFormat(precision),

/Users/Doran/anaconda2/lib/python2.7/site-packages/numpy/core/arrayprint.pyc in __init__(self, data)
    635     def __init__(self, data):
    636         try:
--> 637             max_str_len = max(len(str(maximum.reduce(data))),
    638                               len(str(minimum.reduce(data))))
    639             self.format = '%' + str(max_str_len) + 'd'

KeyboardInterrupt: 

```

