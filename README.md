# Simple search project using Youtube-8m dataset and ElasticSearch

[YouTube-8m](https://research.google.com/youtube8m/) dataset is a large-scale labeled video collection that consists of 8 million YouTube video IDs and associated labels from a diverse vocabulary of 4800 visual entities (aka, "Google Knowledge Graph"). More about Google Knowldege Graph [here](https://www.google.com/intl/bn/insidesearch/features/search/knowledge.html). This project will be in three parts: grab video IDs by Google Knowledge Graph Keywords; retrieving metadata using YouTube API; and sending the data to ElasticSearch.

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


TO DO LIST:
* Make simple front to interact with Elasticsearch (~12/10) 
* Make presentation (~12/11)
* Write whitepaper (~12/11)
