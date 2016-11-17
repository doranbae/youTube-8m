# Download/parse the dataset
1. Download the video level

```
$ mkdir yt8m_video_level
$ cd yt8m_video_level/
$ curl us.data.yt8m.org/0/video_level/train/download.py | python
```
The result looks something like this. Goes on for about forever... after 12 hours, I got 6GB downloaded on my laptop so I stopped.

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

2. Parse dataset
Use code from google group: https://groups.google.com/d/msg/youtube8m-users/yEDzH7EqUf8/EfW0WO3jAgAJ

```
python yt8m_parse.py video /PATH/TO/YOUR/VIDEO/LEVEL/DIR/*.tfrecord
python yt8m_parse.py frame /PATH/TO/YOUR/FRAME/LEVEL/DIR/*.tfrecord
```
