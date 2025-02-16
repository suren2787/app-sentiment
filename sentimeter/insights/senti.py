import json
import time
from pathlib import Path
import os
import pandas as pd
import sys
sys.path.append("../../")
from modules.utility import fileops

print('[INFO] SENTIMENT ANALYSIS - Start.')
reviews_file = './results/reviews-filtered.json'
comments=[]
print('[INFO] SENTIMENT ANALYSIS - Loaded normalized reviews. Filtering comments from Json.')
#Open file and filter only comments
with open(reviews_file, 'r') as ifh:
    reviews = json.load(ifh)

    for review in reviews:
        text=review['translatedcontent']
        if not isinstance(text, str):
            text=''
        comments.append(text)
print('[INFO] SENTIMENT ANALYSIS - Separated comments. Sentiment analysis is in progress')

#get sentiments of comments
from transformers import pipeline
# sentiment_pipeline = pipeline("text-classification",model='bhadresh-savani/distilbert-base-uncased-emotion')
sentiment_pipeline = pipeline("sentiment-analysis", model='distilbert/distilbert-base-uncased-finetuned-sst-2-english')
data = comments
result = sentiment_pipeline(data)
print('[INFO] SENTIMENT ANALYSIS - sentiments analyzed. Saving File as json')

#save sentiments
#construct filename
time_str = time.strftime("%Y%m%d-%H%M%S")
file_name_str = "results/reviews-sentiments.json"
backup_filename_str="results/reviews-sentiments-backup-"+time_str+".json"

#check if file exists
fileops.renamefile(file_name_str,backup_filename_str)

# # Writing to sample.json
json_object = json.dumps(result, indent=4,default=str)
fileops.savefile(file_name_str,json_object)

print('[INFO] SENTIMENT ANALYSIS - All steps completed')
