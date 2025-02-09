import json
import time
from pathlib import Path
import os
import pandas as pd
import sys
sys.path.append("../../")
from modules.utility import fileops

print('[INFO] senti - Start.')
reviews_file = '../datacollection/results/reviews-normalized.json'
comments=[]
print('[INFO] senti - Loaded normalized reviews. Filtering comments from Json.')
#Open file and filter only comments
with open(reviews_file, 'r') as ifh:
    reviews = json.load(ifh)

    for review in reviews:
        text=review['translatedcontent']
        if not isinstance(text, str):
            text=''
        comments.append(text)
print('[INFO] senti - Filtered comments. Text Classification analysis is in progress')

#get sentiments of comments
from transformers import pipeline

classifier_pipeline = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
categories = ["UI/UX", "Performance", "Bugs", "Feature Requests","Customer Support"]
data = comments
category_result = classifier_pipeline(data, candidate_labels=categories)
print("Category:", category_result['labels'][0])
print('[INFO] senti - Classified comments. Saving File as json')
#save sentiments
#construct filename
time_str = time.strftime("%Y%m%d-%H%M%S")
file_name_str = "results/reviews-sentimeter.json"
backup_filename_str="results/reviews-sentimeter-backup-"+time_str+".json"

#check if file exists
fileops.renamefile(file_name_str,backup_filename_str)

# # Writing to sample.json
json_object = json.dumps(category_result, indent=4,default=str)
fileops.savefile(file_name_str,json_object)

print('[INFO] senti - All steps completed')
