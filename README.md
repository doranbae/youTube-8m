# Simple search project using Youtube-8m dataset and ElasticSearch

[YouTube-8m](https://research.google.com/youtube8m/) dataset is a large-scale labeled video collection that consists of 8 million YouTube video IDs and associated labels from a diverse vocabulary of 4800 visual entities (aka, "Google Knowledge Graph"). More about Google Knowldege Graph [here](https://www.google.com/intl/bn/insidesearch/features/search/knowledge.html). 

## 1. Prerequisites
#### Requirements
* ElasticSearch: Install instructions TBU
* Python packages

## 2. Prepare data
#### Instructions (for a test-run, using a small subset of the entire dataset)
* Copy `retrieveData.py` and `push2ES.py` into a directory
* Run `push2ES.py` in python
```
python push2ES.py
```
#### Instructions (using full dataset)
* Copy `retrieveData.py` and `push2ES.py` into a directory
* Open `retrieveData.py`
* In line 189, edit `sampleSeries` to `totalSeries` and save the file
* Run `push2ES.py` in python
```
python push2ES.py
```
#### Instructions (using batch file)
* Go to `push2ES_batch` folder
* Copy `retrieveData_batch.py` and `push2ES_batch.py` into a directory
* Open `push2ES.py`
* I've changed the code to send DataFrame to ElasticSearch 4800 times, 1 for every knowledge tree entities. 
```
i=4700

while i < 4705:
    print(i)
    pushCall = push2ES(i)
    pushCall.pushToES()
    i=i+1
else:
    print("Done")
```
* Right now, it is set to send DataFrame to ElasticSearch 5 times from entity[4700] ~ entity[4705]
* Now I think about it, I think we can make the batch for every 100 entities or so
* In while loop, every batch gets updated to ElasticSearch. But once I stop the script, and re-run it, it doesn't get updated. So if you are testing multiple times, be sure to delete ElasticSearch index
```
curl -XDELETE localhost:9200/youtube
```
* Run `push2ES_batch.py` in python
```
python push2ES_batch.py
```




TO DO LIST:
* Make simple front to interact with Elasticsearch (~12/10) 
* Make presentation (~12/11)
* Write whitepaper (~12/11)
