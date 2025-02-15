import json
import pandas as pd
import sys
sys.path.append("../../")
from modules.appstore import asreviews
from modules.translate import langtranslate
import config

def normalized_reviews():
    appreviews = asreviews.reviews(country=config.appstore['country'], appname=config.appstore['appname'], appid=config.appstore['appid'] )
    normalized_reviews=[]

    reviews = json.loads(appreviews)

    #Translate to English
    comments = []
    for review in reviews:
            comments.append(review['review'])

    print('[INFO] datacollection - Appstore Comments collected for translation. Translation in progress.')
    translatedcomments = langtranslate.translate(sourcelang="auto", targetlang="en", textarray=comments)

    print('[INFO] datacollection - Translation completed. Normalization in progress.')
    for i,review in enumerate(reviews):
        if 'developerResponse' in review:
            normalized_reviews.append({
                'reviewid':'',
                'reviewdate':review['date'],
                'username':review['userName'],
                'rating':review['rating'],
                'title':review['title'],
                'content':review['review'],
                'translatedcontent':translatedcomments[i],
                'appversion':'',
                'responsecontent':review['developerResponse']['body'],
                'responsedate':review['developerResponse']['modified'],
                'source':'Appstore'
            })
        else:
            normalized_reviews.append({
                'reviewid':'',
                'reviewdate':review['date'],
                'username':review['userName'],
                'rating':review['rating'],
                'title':review['title'],
                'content':review['review'],
                'translatedcontent':translatedcomments[i],
                'appversion':'',
                'responsecontent':'',
                'responsedate':'',
                'source':'Appstore'
            })
    print('[INFO] datacollection - Normalization completed.')
    return normalized_reviews

print('[INFO] datacollection - All steps completed')

