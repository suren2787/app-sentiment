import json
import time
import pandas as pd
import sys
sys.path.append("../../")
from modules.playstore import psreviews
from modules.utility import fileops
from modules.translate import *
import config

# app_store_reviews_file = '../../modules/playstore-scraper/results/ps-reviews.json'
appreviews = psreviews.reviews(country=config.playstore['country'], appname=config.playstore['appname'])
normalized_reviews=[]

# with open(app_store_reviews_file, 'r') as ifh:
#     reviews = json.load(ifh)
reviews = json.loads(appreviews)
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

#construct filename
time_str = time.strftime("%Y%m%d-%H%M%S")
file_name_str = "results/ps-normalized.json"
backup_filename_str="results/ps-normalized-backup-"+time_str+".json"

#check if file exists
fileops.renamefile(file_name_str,backup_filename_str)

# # Writing to sample.json
json_object = json.dumps(normalized_reviews, indent=4,default=str)
fileops.savefile(file_name_str,json_object)

