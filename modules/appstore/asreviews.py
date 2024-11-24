import pandas as pd
import numpy as np
import json
from app_store_scraper import AppStore

def reviews(country, appname, appid):
  result = AppStore(country=country, app_name=appname, app_id = appid)
  result.review()
  result.reviews.sort(key=sortFn, reverse=True)
  json_object = json.dumps(result.reviews, indent=4,default=str)
  return json_object

def sortFn(dict):
  return dict['date']
  

# print(reviews(country='hk', appname='mox-bank', appid = '1505743481'))