import json
import time
from datetime import datetime
from pathlib import Path
import os
import pandas as pd
import sys
sys.path.append("../../")
from modules.utility import fileops

print('[INFO] summarization - Start.')
reviews_file = 'results/summary.json'
comments_current=""
comments_current_1=""
comments_current_2=""
current_month = datetime.now().month
current_year = datetime.now().year

comments_array=[]
comments_array_1=[]
comments_array_2=[]

print('[INFO] summarization - Loaded normalized reviews. Filtering comments from Json.')
#Open file and filter only comments
with open(reviews_file, 'r') as ifh:
    reviews = json.load(ifh)

    for review in reviews:
        text=review['translatedcontent']
        reviewdate=datetime.strptime(review['reviewdate'],'%Y-%m-%d %H:%M:%S').date()
        sentiment=review['sentiment']
        if not isinstance(text, str):
            text=''

        if(sentiment=='NEGATIVE' and reviewdate.year==current_year):                                                                      
            if(reviewdate.month==current_month):
                comments_current = comments_current + "\n" + text #comments.join(text)
                comments_array.append(text)
            if(reviewdate.month==current_month-1):
                comments_current_1 = comments_current_1 + "\n" + text 
                comments_array_1.append(text)
            if(reviewdate.month==current_month-2):
                comments_current_2 = comments_current_2 + "\n" + text 
                comments_array_2.append(text)
print('[INFO] summarization - Filtered comments. Summary analysis is in progress')
#get summary of comments
from transformers import pipeline

classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
categories = ["UI/UX", "Unstable App", "Unfair Charges", "Slow", "Customer Service"]
category_result = classifier(comments_array_1, candidate_labels=categories)
# Print the results
for i, result in enumerate(category_result):
    print(f"Feedback: {comments_array_1[i]}")
    print(f"Predicted Category: {result['labels'][0]} (Score: {result['scores'][0]:.2f})")
    print()

# summarizer = pipeline(task="summarization")
# result = summarizer(comments_current_1)
# result2 = summarizer(comments_current_2)
# print("-------------------------------------------------")
# print(comments_current_1)
# print("-------------------------------------------------")
# print(result)
# print("-------------------------------------------------")
# print(comments_current_2)
# print("-------------------------------------------------")
# print(result2)
# print("-------------------------------------------------")
# print('[INFO] summarization - sentiments analyzed. Saving File as json')

#save sentiments
#construct filename
time_str = time.strftime("%Y%m%d-%H%M%S")
file_name_str = "results/reviews-current.txt"
backup_filename_str="results/reviews-current-backup-"+time_str+".txt"
file_name_str_lastmonth = "results/reviews-current-1.txt"
backup_filename_str_lastmonth="results/reviews-current-1-backup-"+time_str+".txt"
file_name_str_lastbefore = "results/reviews-current-2.txt"
backup_filename_str_lastbefore ="results/reviews-current-2-backup-"+time_str+".txt"

#check if file exists
fileops.renamefile(file_name_str,backup_filename_str)
fileops.renamefile(file_name_str_lastmonth,backup_filename_str_lastmonth)
fileops.renamefile(file_name_str_lastbefore,backup_filename_str_lastbefore)

# # Writing to sample.json
fileops.savefile(file_name_str,comments_current)
fileops.savefile(file_name_str_lastmonth,comments_current_1)
fileops.savefile(file_name_str_lastbefore,comments_current_2)
print('[INFO] summarization - All steps completed')
