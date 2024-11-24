import json
import pandas as pd
import sys
sys.path.append("../../")
from modules.playstore import psreviews
from modules.translate import langtranslate
import config

def normalized_reviews():
    # app_store_reviews_file = '../../modules/playstore-scraper/results/ps-reviews.json'
    appreviews = psreviews.reviews(country=config.playstore['country'], appname=config.playstore['appname'])
    normalized_reviews=[]

    # with open(app_store_reviews_file, 'r') as ifh:
    #     reviews = json.load(ifh)
    reviews = json.loads(appreviews)

    #Translate to English
    comments = []
    for review in reviews:
            comments.append(review['content'])

    print('[INFO] datacollection - Comments collected for translation. Translation in progress.')
    translatedcomments = langtranslate.translate(sourcelang="auto", targetlang="en", textarray=comments)

    print('[INFO] datacollection - Translation completed. Normalization in progress.')
    for i,review in enumerate(reviews):
        normalized_reviews.append({
            'reviewid':review['reviewId'],
            'reviewdate':review['at'],
            'username':review['userName'],
            'rating':review['score'],
            'title':'',
            'content':review['content'],
            'translatedcontent':translatedcomments[i],
            'appversion':review['appVersion'],
            'responsecontent':review['replyContent'],
            'responsedate':review['repliedAt'],
            'source':'Playstore'
        })
    print('[INFO] datacollection - Normalization completed.')
    return normalized_reviews

print('[INFO] datacollection - All steps completed')
