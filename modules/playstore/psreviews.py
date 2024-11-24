import time
from google_play_scraper import Sort, reviews_all
import json
from pathlib import Path
import os

def reviews(country, appname):
    result = reviews_all(
        appname,
        sleep_milliseconds=0, # defaults to 0
        lang='en', # defaults to 'en'
        country=country, # defaults to 'us'
        sort=Sort.NEWEST, # defaults to Sort.MOST_RELEVANT
        # filter_score_with=5 # defaults to None(means all score)
    )
    json_object = json.dumps(result, indent=4,default=str)
    return json_object


# print(reviews(country='hk', appname='com.mox.app'))
