import json
import time
from pathlib import Path
from datetime import datetime,timedelta
import os
import pandas as pd
import sys
sys.path.append("../../")
from modules.utility import fileops
from collections import defaultdict


print('[INFO] SUMMARY ANALYSIS - Start.')

reviews_file = 'results/reviews-filtered.json'
sentimeter_file = 'results/reviews-sentiments.json'
category_file = 'results/reviews-category.json'
summary=[]
positive_comments_1=""
negative_comments_1=""
positive_comments_2=""
negative_comments_2=""
positive_comments_3=""
negative_comments_3=""
print(datetime.today().month)
with open(sentimeter_file, 'r') as ifh:
    sentiments = json.load(ifh)

with open(reviews_file, 'r') as ifh:
    reviews = json.load(ifh)

with open(category_file, 'r') as ifh:
    categories = json.load(ifh)

    for i,review in enumerate(reviews):
        summary.append({
            'reviewid':review['reviewid'],
            'reviewdate':review['reviewdate'],
            'username':review['username'],
            'rating':review['rating'],
            'title':'',
            'appversion':review['appversion'],
            'responsecontent':review['responsecontent'],
            'responsedate':review['responsedate'],
            'source':review['source'],
            'content':review['content'],
            'translatedcontent':review['translatedcontent'],
            'predictedsentiment':sentiments[i]['label'],
            'predictedcategory':categories[i]['labels'][0]
        })
        reviewdate = datetime.strptime(review["reviewdate"], "%Y-%m-%d %H:%M:%S")
        if(reviewdate.month == datetime.today().month):
        
            if sentiments[i]['label'] == "POSITIVE" :
                positive_comments_1 = positive_comments_1 + "/n" + review['translatedcontent']
            else :
                negative_comments_1 = negative_comments_1 + "/n" + review['translatedcontent']
        if(reviewdate.month == datetime.today().month-1):
        
            if sentiments[i]['label'] == "POSITIVE" :
                positive_comments_2 = positive_comments_2 + "/n" + review['translatedcontent']
            else :
                negative_comments_2 = negative_comments_2 + "/n" + review['translatedcontent']
        if(reviewdate.month == datetime.today().month-2):
        
            if sentiments[i]['label'] == "POSITIVE" :
                positive_comments_3 = positive_comments_3 + "/n" + review['translatedcontent']
            else :
                negative_comments_3 = negative_comments_3 + "/n" + review['translatedcontent']


from transformers import pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn") 


positive_summary_text_1 = summarizer(
                positive_comments_1,
                max_length=100,
                min_length=30,
                do_sample=False
            )[0]["summary_text"]
negative_summary_text_1 = summarizer(
                negative_comments_1,
                max_length=100,
                min_length=30,
                do_sample=False
            )[0]["summary_text"]
positive_summary_text_2 = summarizer(
                positive_comments_2,
                max_length=100,
                min_length=30,
                do_sample=False
            )[0]["summary_text"]
negative_summary_text_2 = summarizer(
                negative_comments_2,
                max_length=100,
                min_length=30,
                do_sample=False
            )[0]["summary_text"]

positive_summary_text_3 = summarizer(
                positive_comments_3,
                max_length=100,
                min_length=30,
                do_sample=False
            )[0]["summary_text"]
negative_summary_text_3 = summarizer(
                negative_comments_3,
                max_length=100,
                min_length=30,
                do_sample=False
            )[0]["summary_text"]

print("comments:"+ positive_comments_1)
print(positive_summary_text_1)

print("---------------------------------------------------------------------")
print("comments:"+ positive_comments_2)
print(positive_summary_text_2)
print("---------------------------------------------------------------------")
print("comments:"+ positive_comments_3)
print(positive_summary_text_3)
print("---------------------------------------------------------------------")
print("comments:"+ negative_comments_1)
print(negative_summary_text_1)
print("---------------------------------------------------------------------")
print("comments:"+ negative_comments_2)
print(negative_summary_text_2)
print("---------------------------------------------------------------------")
print("comments:"+ negative_comments_3)
print(negative_summary_text_3)
# def generate_summary(label, category_data):
#     summary_text = []
#     for comments in category_data.items():
#         if comments:
#             # Join comments into a single text for summarization
#             combined_text = " ".join(comments)
#             # Generate a summary for the category
#             summary_text = summarizer(
#                 combined_text,
#                 max_length=100,
#                 min_length=30,
#                 do_sample=False
#             )[0]["summary_text"]
#             summary.append(f"**{category}**: {summary_text}")
#     return "\n".join(summary)
# # positive_summary = generate_summary("positive", results["positive"])
# negative_summary = generate_summary("negative", results["negative"])

# with open("executive_summary.md", "w") as f:
#     f.write(executive_summary)

#save sentiments
#construct filename
time_str = time.strftime("%Y%m%d-%H%M%S")
file_name_str = "results/reviews-summary.json"
backup_filename_str="results/reviews-summary-backup-"+time_str+".json"

#check if file exists
fileops.renamefile(file_name_str,backup_filename_str)

# # Writing to sample.json
json_object = json.dumps(summary, indent=4,default=str)
fileops.savefile(file_name_str,json_object)

print('[INFO] SUMMARY ANALYSIS - All steps completed')
