import json
import time
from pathlib import Path
import os
import pandas as pd

play_store_reviews_file = '../../playstore-scraper/results/ps-reviews.json'
play_store_sentimeter_file = 'results/ps-sentimeter.json'

summary=[]

with open(play_store_sentimeter_file, 'r') as ifh:
    sentiments = json.load(ifh)


with open(play_store_reviews_file, 'r') as ifh:
    reviews = json.load(ifh)



    for i,review in enumerate(reviews):
        summary.append({'reviewId': review['reviewId'],
        'userName':review['userName'],
        'userImage':review['userImage'],
        'content':review['content'],
        'sentiment':sentiments[i]['label'],
        'score':review['score'],
        'thumbsUpCount':review['thumbsUpCount'],
        'reviewCreatedVersion':review['reviewCreatedVersion'],
        'at':review['at'],
        'replyContent':review['replyContent'],
        'repliedAt':review['repliedAt'],
        'appVersion':review['appVersion'],
        })

#save Summary
#construct filename
time_str = time.strftime("%Y%m%d-%H%M%S")
file_name_str = "results/ps-Summary.json"
backup_filename_str="results/ps-Summary-backup-"+time_str+".json"

#check if file exists
curr_file = Path(file_name_str)
if curr_file.is_file():
    os.rename(file_name_str,backup_filename_str)

# # Writing to sample.json
json_object = json.dumps(summary, indent=4,default=str)
with open(file_name_str, "w") as outfile:
    outfile.write(json_object)

print("Summary file saved successfully")

# save as html
time_str = time.strftime("%Y%m%d-%H%M%S")
file_name_str = "results/ps-Summary.html"
backup_filename_str="results/ps-Summary-backup-"+time_str+".html"

#check if file exists
curr_file = Path(file_name_str)
if curr_file.is_file():
    os.rename(file_name_str,backup_filename_str)

from json2html import *
with open(file_name_str, "w", encoding="utf-8") as outfile:
    outfile.write(json2html.convert(json = json_object))
print("html file generated") 
