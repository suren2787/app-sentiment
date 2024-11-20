import pandas as pd
import numpy as np
import json
import time
from pathlib import Path
import os

from app_store_scraper import AppStore
result = AppStore(country='hk', app_name='mox-bank', app_id = '1505743481')

result.review()

def sortFn(dict):
  return dict['date']
  
reviews = result.reviews.sort(key=sortFn, reverse=True)

#construct filename
time_str = time.strftime("%Y%m%d-%H%M%S")
file_name_str = "results/as-reviews.json"
backup_filename_str="results/as-reviews-backup-"+time_str+".json"


def renamefile(file_name_str, backup_filename_str):
    curr_file = Path(file_name_str)
    if curr_file.is_file():
        os.rename(file_name_str,backup_filename_str)

# # Writing to sample.json
def savefile(file_name_str, json_object):
    with open(file_name_str, "w") as outfile:
        outfile.write(json_object)


#check if file exists
renamefile(file_name_str,backup_filename_str)

# # Writing to sample.json
json_object = json.dumps(result.reviews, indent=4,default=str)
savefile(file_name_str,json_object)