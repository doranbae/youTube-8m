# Simple search project using Youtube-8m dataset and ElasticSearch

[YouTube-8m](https://research.google.com/youtube8m/) dataset is a large-scale labeled video collection that consists of 8 million YouTube video IDs and associated labels from a diverse vocabulary of 4800 visual entities (aka, "Google Knowledge Graph"). More about Google Knowldege Graph [here](https://www.google.com/intl/bn/insidesearch/features/search/knowledge.html). 

## Prerequisites
#### Requirements
* HDFS
* ElasticSearch
* Kibana 

#### Provision VMs
* XGB memory
* 100 disk

## Part 1: Index the Youtube-8M (source) dataset with ElasticSearch 
#### Instructions 
* Copy `push2ES_batch2.py` and `pretrieveData_batch2.py` into a directory
* Run `push2ES_batch2.py` in python
```
python push2ES_batch2.py
```

#### FIXES

* use `push2ES_batch2.py` and `retrieveData_batch2.py`
* fixed index id numbering and added column information (description, rating, likes, dislikes, author, published, etc.)
* added exception handling

## Part 2: Explore analytics using Kibana


## Part 3: Export Youtube-8M tensorflow files for future machine learning analysis
