import json
import time
from pathlib import Path
import os
import pandas as pd

app_store_reviews_file = '../../playstore-scraper/results/ps-reviews.json'
normalized_reviews=[]

with open(app_store_reviews_file, 'r') as ifh:
    reviews = json.load(ifh)

#Open file and filter only comments
    for review in reviews:
        normalized_reviews.append({
            'reviewid':review['reviewId'],
            'reviewdate':review['at'],
            'username':review['userName'],
            'rating':review['score'],
            'title':'',
            'content':review['content'],
            'appversion':review['appVersion'],
            'responsecontent':review['replyContent'],
            'responsedate':review['repliedAt'],
        })

def renamefile(file_name_str, backup_filename_str):
    curr_file = Path(file_name_str)
    if curr_file.is_file():
        os.rename(file_name_str,backup_filename_str)

# # Writing to sample.json
def savefile(file_name_str, json_object):
    with open(file_name_str, "w") as outfile:
        outfile.write(json_object)

#construct filename
time_str = time.strftime("%Y%m%d-%H%M%S")
file_name_str = "results/ps-normalized.json"
backup_filename_str="results/ps-normalized-backup-"+time_str+".json"

#check if file exists
renamefile(file_name_str,backup_filename_str)

# # Writing to sample.json
json_object = json.dumps(normalized_reviews, indent=4,default=str)
savefile(file_name_str,json_object)

