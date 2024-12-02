import json
import time
from datetime import datetime
from pathlib import Path
import os
import pandas as pd
import sys
sys.path.append("../../")
from modules.utility import fileops

print('[INFO] summarization - Start.')
reviews_file = 'results/summary.json'
comments_Current=""
comments_current_1=""
comments_current_2=""
current_month = datetime.now().month
current_year = datetime.now().year

print('[INFO] summarization - Loaded normalized reviews. Filtering comments from Json.')
#Open file and filter only comments
with open(reviews_file, 'r') as ifh:
    reviews = json.load(ifh)

    for review in reviews:
        text=review['translatedcontent']
        reviewdate=datetime.strptime(review['reviewdate'],'%Y-%m-%d %H:%M:%S').date()
        sentiment=review['sentiment']
        if not isinstance(text, str):
            text=''

        if(sentiment=='NEGATIVE' and reviewdate.year==current_year):                                                                      
            if(reviewdate.month==current_month):
                comments_Current = comments_Current + "\n" + text #comments.join(text)
            if(reviewdate.month==current_month-1):
                comments_current_1 = comments_current_1 + "\n" + text 
            if(reviewdate.month==current_month-2):
                comments_current_2 = comments_current_2 + "\n" + text 
print('[INFO] summarization - Filtered comments. Sentiment analysis is in progress')
#get summary of comments
from transformers import pipeline

summarizer = pipeline(task="summarization")
result = summarizer(comments_current_1)
result2 = summarizer(comments_current_2)
print("-------------------------------------------------")
print(comments_current_1)
print("-------------------------------------------------")
print(result)
print("-------------------------------------------------")
print(comments_current_2)
print("-------------------------------------------------")
print(result2)
print("-------------------------------------------------")
print('[INFO] summarization - sentiments analyzed. Saving File as json')

# #save sentiments
# #construct filename
# time_str = time.strftime("%Y%m%d-%H%M%S")
# file_name_str = "results/reviews-sentimeter.json"
# backup_filename_str="results/reviews-sentimeter-backup-"+time_str+".json"

# #check if file exists
# fileops.renamefile(file_name_str,backup_filename_str)

# # # Writing to sample.json
# json_object = json.dumps(result, indent=4,default=str)
# fileops.savefile(file_name_str,json_object)

# print('[INFO] summarization - All steps completed')
