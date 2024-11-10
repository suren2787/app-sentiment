import time
from google_play_scraper import Sort, reviews_all
import json
from pathlib import Path
import os

result = reviews_all(
    'com.mox.app',
    sleep_milliseconds=0, # defaults to 0
    lang='en', # defaults to 'en'
    country='hk', # defaults to 'us'
    sort=Sort.NEWEST, # defaults to Sort.MOST_RELEVANT
    # filter_score_with=5 # defaults to None(means all score)
)
#construct filename
time_str = time.strftime("%Y%m%d-%H%M%S")
file_name_str = "results/ps-reviews.json"
backup_filename_str="results/ps-reviews-backup-"+time_str+".json"

#check if file exists
curr_file = Path(file_name_str)
if curr_file.is_file():
    os.rename(file_name_str,backup_filename_str)

# # Writing to sample.json
json_object = json.dumps(result, indent=4,default=str)
with open(file_name_str, "w") as outfile:
    outfile.write(json_object)
