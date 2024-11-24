import json
import time
import pandas as pd
import sys
sys.path.append("../../")
from modules.utility import fileops
import prepareappstorereviews as appstore
import prepareplaystorereviews as playstore

print('[INFO] generatedata - Started')
print('[INFO] generatedata - Collecting Appstore reviews')
normalized_reviews = appstore.normalized_reviews()

print('[INFO] generatedata - Collecting Playstore reviews')
normalized_reviews.append(playstore.normalized_reviews())

print('[INFO] generatedata - Saving File as json')
#construct filename
time_str = time.strftime("%Y%m%d-%H%M%S")
file_name_str = "results/reviews-normalized.json"
backup_filename_str="results/reviews-normalized-backup-"+time_str+".json"

#check if file exists
fileops.renamefile(file_name_str,backup_filename_str)

# # Writing to sample.json
json_object = json.dumps(normalized_reviews, indent=4,default=str)
fileops.savefile(file_name_str,json_object)

print('[INFO] generatedata - All steps completed')