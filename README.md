# Simple search project using Youtube-8m dataset and ElasticSearch

[YouTube-8m](https://research.google.com/youtube8m/) dataset is a large-scale labeled video collection that consists of 8 million YouTube video IDs and associated labels from a diverse vocabulary of 4800 visual entities (aka, "Google Knowledge Graph"). More about Google Knowldege Graph [here](https://www.google.com/intl/bn/insidesearch/features/search/knowledge.html). 

## Prerequisites
#### Requirements
* Swift
* ElasticSearch
* Kibana 
* Python libraries: pafy, csv, json, itertools, pandas, numpy, requests, urllib

#### Provision VMs
* Hardware: 8 CPU, 32 GB
* Connection: 100 GB local, 1GB network

## Part 1: Index the Youtube-8M (source) dataset with ElasticSearch 
#### Instructions 
* Copy `push2ES_batch2.py` , `retrieveData_batch2.py` into a directory
* Execute `batchrunpy2.sh`

This shell script is to simultaneously run 100 and 84 instances respectively of the `push2ES_batch2.py` script


## Part 2: Explore analytics using Kibana


## Part 3: Export Youtube-8M tensorflow files for future machine learning analysis


## Change Log

### YouTube Retrieve Metadata + Push to ES

#### Version 1
* Base files to retrieve metadata from a sample subset to run locally on computer

#### Version 2
* Cleaned code for easier viewing and debugging
* Updated so that code is able to run the full set

#### Version 3
* Fixed index id numbering and added column information (description, rating, likes, dislikes, author, published, etc.)
* Added exception handling for invalid YouTube data

#### Version 4
* Fixed thumbnail retrieval portion that was not working
* Fixed try/except loop that was exiting prematurely with an error (was previously unable to go through all videos in the given document)
* Modified so that `push2ES_batch.py` takes two system arguments to specify which documents to process


### Shell Script batchrunpy, batchrunpy2

#### Version 1
* Created shell scripts to simultaneously run 100 and 84 instances respectively of the `push2ES_batch.py` script 

#### Version 2
* Crash because all of the instances were starting and logging into the YouTube API at the same time
* Added "sleep" and "nohup" to the command chains so there is a staggered start
