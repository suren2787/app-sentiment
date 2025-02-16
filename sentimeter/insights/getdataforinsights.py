import json
import time
from datetime import datetime,timedelta
from dateutil.relativedelta import relativedelta
import sys
sys.path.append("../../")
from modules.utility import fileops

print('[INFO] FILTER REVIEWS - Start')
today = datetime.today()
report_last_x_months = 6
x_months = today + relativedelta(months=-report_last_x_months)
x_months = x_months + timedelta(days=-x_months.day+1) 
x_months = x_months.replace(hour=0, minute=0, second=0, microsecond=0)

print('[INFO] FILTER REVIEWS - Filtering data from {x_months}')


# Load JSON data
all_reviews = ''

reviews_file = '../datacollection/results/reviews-normalized.json'
with open(reviews_file, 'r') as ifh:
    all_reviews = json.load(ifh)

# Filter data based on the date field
filtered_data = []

for review in all_reviews:
    if datetime.strptime(review["reviewdate"], "%Y-%m-%d %H:%M:%S") >= x_months:
        filtered_data.append(review)


print('[INFO] FILTER REVIEWS - Filtered Reviews. Saving File as json')
#save reviews
#construct filename
time_str = time.strftime("%Y%m%d-%H%M%S")
file_name_str = "results/reviews-filtered.json"
backup_filename_str="results/reviews-filtered-backup-"+time_str+".json"

#check if file exists
fileops.renamefile(file_name_str,backup_filename_str)

# # Writing to sample.json
json_object = json.dumps(filtered_data, indent=4,default=str)
fileops.savefile(file_name_str,json_object)
print('[INFO] FILTER REVIEWS - All steps completed')
