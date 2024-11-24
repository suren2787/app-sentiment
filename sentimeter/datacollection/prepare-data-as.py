import json
import time
import pandas as pd
import sys
sys.path.append("../../")
from modules.appstore import asreviews
from modules.utility import fileops
from modules.translate import *
import config

# app_store_reviews_file = '../../modules/appstore-scraper/results/as-reviews.json'
appreviews = asreviews.reviews(country=config.appstore['country'], appname=config.appstore['appname'], appid=config.appstore['appid'] )
normalized_reviews=[]
# with open(app_store_reviews_file, 'r') as ifh:
#     reviews = json.load(ifh)
reviews = json.loads(appreviews)

#Open file and filter only comments
for review in reviews:
    if 'developerResponse' in review:
        normalized_reviews.append({
            'reviewid':'',
            'reviewdate':review['date'],
            'username':review['userName'],
            'rating':review['rating'],
            'title':review['title'],
            'content':review['review'],
            'appversion':'',
            'responsecontent':review['developerResponse']['body'],
            'responsedate':review['developerResponse']['modified']
        })
    else:
        normalized_reviews.append({
            'reviewid':'',
            'reviewdate':review['date'],
            'username':review['userName'],
            'rating':review['rating'],
            'title':review['title'],
            'content':review['review'],
            'appversion':'',
            'responsecontent':'',
            'responsedate':''
        })

#construct filename
time_str = time.strftime("%Y%m%d-%H%M%S")
file_name_str = "results/as-normalized.json"
backup_filename_str="results/as-normalized-backup-"+time_str+".json"

#check if file exists
fileops.renamefile(file_name_str,backup_filename_str)

# # Writing to sample.json
json_object = json.dumps(normalized_reviews, indent=4,default=str)
fileops.savefile(file_name_str,json_object)

