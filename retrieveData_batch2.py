# 1. Download the video IDs by Google Knowledge Graph Keywords

# What do I need?
import requests
import urllib
import numpy as np
import pandas as pd
import pafy # A handy package that retrieves YouTube content and metadata
import csv
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8') # For displaying foreign characters
from itertools import repeat

class retrieveAPIData :

    def __init__(self):
        # Set my YouTube API Key
        pafy.set_api_key("AIzaSyCnrbLP8V3zdMwG9kaTaCmeq49nNqyEpZ8")
        urllib.URLopener().retrieve("http://research.google.com/youtube8m/csv/train-labels-histogram.csv" , "labels.csv")

        #data variables
        self.sampleSeries = []
        self.totalSeries = []
        self.videoList = []
        self.emptyFrames = []

        self.tFrame = pd.DataFrame()

    def getDataFromCSV(self):
        # Transform the csv file into a usalbe format.
        # Read "labels.csv" and save it into a DataFrame.
        df1 = pd.read_csv('labels.csv')
        return df1

    def getPDLabelsID(self):

        df1 = self.getDataFromCSV()

        # We only need labelsID, label Name and First vertical
        labelsID = df1[['KnowledgeGraphID', 'LabelName', 'FirstVertical']]
        # print("## Original labels list looks like this:")
        # print(labelsID.head(n=4))
        return labelsID

    def getPDSeriesData(self):

        labelsID = self.getPDLabelsID()

        # Remove '/m/' from labelsID column
        series = labelsID["KnowledgeGraphID"]
        series = series.str.replace('/m/', '')

        # Make a copy for a later use.
        series_copy = pd.concat([labelsID, series], axis=1)
        series_copy["key"] = series_copy[[3]]
        series_copy = series_copy.drop("KnowledgeGraphID", axis=1)

        #print("After data cleansing")
        #print("Total number of labels:", series.shape)
        #print(series_copy.head(n=4))

        return series_copy

    def readFromCSV(self, index):

        labelsID = self.getPDLabelsID()

        # Remove '/m/' from labelsID column
        series = labelsID["KnowledgeGraphID"]
        series = series.str.replace('/m/','')

        self.totalSeries = series
        # Make Video IDs into a list
        # For simplicity, I used "series_sample" which is a small subset of the entire 4800 labels.
        #series_sample = series[4797:4799]
        series_sample = series[index:index+1]

        self.sampleSeries = series_sample

        #print("These are samples:")
        #print(series_sample)

    def getLabelVideoIDs(self):

        labels_videoIDs = pd.concat(self.emptyFrames)

        #print(labels_videoIDs.head(n=4))
        #print(labels_videoIDs.tail(n=4))
        #print("The total number of video IDs: ")
        #print(labels_videoIDs.shape)

        return labels_videoIDs

# Iterate the series list to get video IDs for all labels.
    def createVideoList(self, series_data):
        LabelsList = series_data
        total_list = []
        total_k = []
        empty_frames = []

        for k in LabelsList:
            call_kg_page = requests.get("http://storage.googleapis.com/www.yt8m.org/csv/j/%s.js" % k)
            to_string = str(call_kg_page.text)
            n = to_string.count(";")
            to_list = to_string.split(";", n-1)
            list_filter = [list_filter for list_filter in to_list if len(list_filter) == 11]
            total_list.append(list_filter)
            total_list_unnested = sum(total_list, [])
            total_k = list(repeat(k,len(total_list_unnested)))
            #print(total_list_unnested[:10])
            #print(total_k[:10])
            subdt1 = pd.DataFrame({
                    'vID': total_list_unnested,
                    'key': total_k})
            empty_frames.append(subdt1)

        self.emptyFrames = empty_frames

        labels_videoIDs = self.getLabelVideoIDs()

        # Transform into list
        VideoIDList = labels_videoIDs["vID"].tolist()

        self.videoList = VideoIDList

        #print("The total number of video IDs list:")
        #print(len(VideoIDList))

    # Using video IDs, retrieve YouTube metadata
    # Set VideoIDList to video
    def retrieveMetaData(self):

        video = self.videoList

        # Set metadata
        vid_ID = []
        title = []
        thumbnail = []
        rating = []
        viewcount = []
        author = []
        length = []
        duration = []
        likes = []
        dislikes = []
        description = []
        published = []
        keywords = []
        
        count_vid = 0

        try:
            for v in video:
                #vid_url = "https://www.youtube.com/watch?v=%s" % v
                count_vid += 1
                vid = pafy.new(v)
                vid_ID.append(v)
                print (v)
                metalist = [title, thumbnail, rating, viewcount, author, length, duration, likes, dislikes, description, published, keywords]
                metalist_s = ["title", "thumbnail", "rating", "viewcount", "author", "length", "duration", "likes", "dislikes", "description", "published", "keywords"]
                
                i = 0
                for x in metalist:
                  try:
                    to_append = eval("vid." + str(metalist_s[i]))
                    if (x == likes or x == dislikes):
                      x.append(to_append+0.001)
                    else:
                      x.append(to_append)
                  except:
                    x.append("errorappend")
                  i += 1
            
        except:
            e = sys.exc_info()[0]
            print e
            pass
        print "Videoo Count: " + str(count_vid)

        # Save the results in DataFrame
        t = pd.DataFrame(
            {
                'vID': vid_ID,
                'title': title,
                'thumbnail': thumbnail,
                'rating': rating,
                'viewcount': viewcount,
                'author': author,
                'length': length,
                'duration': duration,
                'likes': likes,
                'dislikes': dislikes,
                'description': description,
                'published': published,
                'keywords': keywords})

        # Merge all data into one DataFrame

        labels_IDs = self.getPDLabelsID()
        labels_videoIDs = self.getLabelVideoIDs()

        VideoIDList = labels_videoIDs["vID"].tolist()
        #print("The total number of video IDs list:")
        #print(len(VideoIDList))

        series_copy = self.getPDSeriesData()

        # Merge the DatFrame with appropriate label names
        tt = t.merge(labels_videoIDs, on='vID', how='left')
        ttComplete = tt.merge(series_copy, on='key', how='left')
        # View the DataFrame
        #print(ttComplete.tail(n=4))

        self.tFrame = ttComplete

    @staticmethod
    def main(index):

        if index % 100 == 0 :
            print (index)

        apiCall = retrieveAPIData()
        apiCall.readFromCSV(index)
        apiCall.createVideoList(apiCall.sampleSeries)
        apiCall.retrieveMetaData()

        return apiCall
