import json
import time
from pathlib import Path
import os
import pandas as pd
import sys
sys.path.append("../../")
from modules.utility import fileops
import csv

reviews_file = '../datacollection/results/reviews-normalized.json'
sentimeter_file = 'results/reviews-sentimeter.json'

summary=[]

with open(sentimeter_file, 'r') as ifh:
    sentiments = json.load(ifh)


with open(reviews_file, 'r') as ifh:
    reviews = json.load(ifh)



    for i,review in enumerate(reviews):
        summary.append({
            'reviewid':review['reviewid'],
            'reviewdate':review['reviewdate'],
            'username':review['username'],
            'rating':review['rating'],
            'title':'',
            'content':review['content'],
            'translatedcontent':review['translatedcontent'],
            'sentiment':sentiments[i]['label'],
            'appversion':review['appversion'],
            'responsecontent':review['responsecontent'],
            'responsedate':review['responsedate'],
            'source':review['source']
        })

#save Summary
#construct filename
time_str = time.strftime("%Y%m%d-%H%M%S")
file_name_str = "results/summary.json"
backup_filename_str="results/summary-backup-"+time_str+".json"

#check if file exists
fileops.renamefile(file_name_str,backup_filename_str)

# # Writing to sample.json
json_object = json.dumps(summary, indent=4,default=str)
fileops.savefile(file_name_str,json_object)

print("Summary file saved successfully")

# save as html
time_str = time.strftime("%Y%m%d-%H%M%S")
file_name_str = "results/summary.html"
backup_filename_str="results/summary-backup-"+time_str+".html"

#check if file exists
fileops.renamefile(file_name_str,backup_filename_str)

from json2html import *
with open(file_name_str, "w", encoding="utf-8") as outfile:
    outfile.write(json2html.convert(json = json_object))
print("html file generated") 


 # save as csv
time_str = time.strftime("%Y%m%d-%H%M%S")
file_name_str = "results/summary.csv"
backup_filename_str="results/summary-backup-"+time_str+".csv"

#check if file exists
fileops.renamefile(file_name_str,backup_filename_str)
# now we will open a file for writing
with open(file_name_str, "w", encoding="utf-8") as outfile:

 
    # create the csv writer object
    csv_writer = csv.writer(outfile)
    
    # Counter variable used for writing 
    # headers to the CSV file
    count = 0
    
    for data in summary:
        if count == 0:
    
            # Writing headers of CSV file
            header = data.keys()
            csv_writer.writerow(header)
            count += 1
    
        # Writing data of CSV file
        csv_writer.writerow(data.values())
