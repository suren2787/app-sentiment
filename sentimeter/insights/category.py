import json
import time
from pathlib import Path
import os
import pandas as pd
import sys
sys.path.append("../../")
from modules.utility import fileops

print('[INFO] TEXT CATEGORY ANALYSIS - Start.')
reviews_file = './results/reviews-filtered.json'
comments=[]
print('[INFO] TEXT CATEGORY ANALYSIS - Loaded normalized reviews. Filtering comments from Json.')
#Open file and filter only comments
with open(reviews_file, 'r') as ifh:
    reviews = json.load(ifh)

    for review in reviews:
        text=review['translatedcontent']
        if not isinstance(text, str):
            text=''
        comments.append(text)
print('[INFO] TEXT CATEGORY ANALYSIS - Separated comments. Text Classification analysis is in progress')

#get sentiments of comments
from transformers import pipeline

# Define batch size
batch_size = 20
results = []

classifier_pipeline = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
categories = ["UI/UX", "ENGINEERING", "Customer Support", "OTHERS"]
data = comments

for i in range(0, len(data), batch_size):
    batch = data[i:i + batch_size]  # Get a batch of feedback
    batch_results = classifier_pipeline(batch, candidate_labels=categories)  # Classify the batch
    print('[INFO] TEXT CATEGORY ANALYSIS - Processing Batch {i}')
    results.extend(batch_results)  # Add results to the final list


print('[INFO] TEXT CATEGORY - Categorized comments. Saving File as json')

# for i, result in enumerate(results):
#     print(f"Feedback: {feedback_list[i]}")
#     print(f"Predicted Category: {result['labels'][0]} (Score: {result['scores'][0]:.2f})")
#     print()

#save sentiments
#construct filename
time_str = time.strftime("%Y%m%d-%H%M%S")
file_name_str = "results/reviews-category.json"
backup_filename_str="results/reviews-category-backup-"+time_str+".json"

#check if file exists
fileops.renamefile(file_name_str,backup_filename_str)

# # Writing to sample.json
json_object = json.dumps(results, indent=4,default=str)
fileops.savefile(file_name_str,json_object)

print('[INFO] TEXT CATEGORY ANALYSIS - All steps completed')
