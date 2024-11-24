import json
import time
from pathlib import Path
import os
import pandas as pd

play_store_reviews_file = '../../datacollection/results/as-normalized.json'
comments=[]

#Open file and filter only comments
with open(play_store_reviews_file, 'r') as ifh:
    reviews = json.load(ifh)

    for review in reviews:
        comments.append(review['content'])
print("Successfully read file and filtered Comments")

#get sentiments of comments
from transformers import pipeline
# sentiment_pipeline = pipeline("text-classification",model='bhadresh-savani/distilbert-base-uncased-emotion')
sentiment_pipeline = pipeline("sentiment-analysis")
data = comments
result = sentiment_pipeline(data)
print("sentiments analyzed")

#save sentiments
#construct filename
time_str = time.strftime("%Y%m%d-%H%M%S")
file_name_str = "results/ps-sentimeter.json"
backup_filename_str="results/ps-sentimeter-backup-"+time_str+".json"

#check if file exists
curr_file = Path(file_name_str)
if curr_file.is_file():
    os.rename(file_name_str,backup_filename_str)

# # Writing to sample.json
json_object = json.dumps(result, indent=4,default=str)
with open(file_name_str, "w") as outfile:
    outfile.write(json_object)

print("sentimeter file saved successfully")
