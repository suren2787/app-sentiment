from google_play_scraper import app

result = app(
    'com.app.mox',
    lang='en', # defaults to 'en'
    country='us' # defaults to 'us'
)

print(result)