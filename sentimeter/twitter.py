import tweepy
 
# Add Twitter API key and secret
consumer_key = "P0eA0eSlbBOXoQxzf5Mi0SeP1"
consumer_secret = "it72SEVn7R6xPgQAtZrwgv4agJ2X8FRT32IpFAiKalRLdOOzua"
 
# Handling authentication with Twitter
auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
 
# Create a wrapper for the Twitter API
api = tweepy.API(auth, wait_on_rate_limit=True)

# Helper function for handling pagination in our search and handle rate limits
def limit_handled(cursor):
   while True:
       try:
           yield cursor.next()
       except tweepy.RateLimitError:
           print('Reached rate limite. Sleeping for >15 minutes')
           time.sleep(15 * 61)
       except StopIteration:
           break
 
# Define the term you will be using for searching tweets
query = '#NFTs'
query = query + ' -filter:retweets'
 
# Define how many tweets to get from the Twitter API
count = 1000
 
# Let's search for tweets using Tweepy
search = limit_handled(tweepy.Cursor(api.search_tweets,
                       q=query,
                       tweet_mode='extended',
                       lang='en',
                       result_type="recent").items(count))

from transformers import pipeline
 
# Set up the inference pipeline using a model from the 🤗 Hub
sentiment_analysis = pipeline(model="finiteautomata/bertweet-base-sentiment-analysis")
 
# Let's run the sentiment analysis on each tweet
tweets = []
for tweet in search:
   try:
     content = tweet.full_text
     sentiment = sentiment_analysis(content)
     tweets.append({'tweet': content, 'sentiment': sentiment[0]['label']})
 
   except:
     pass

import pandas as pd
 
# Load the data in a dataframe
df = pd.DataFrame(tweets)
pd.set_option('display.max_colwidth', None)
 
# Show a tweet for each sentiment
display(df[df["sentiment"] == 'POS'].head(1))
display(df[df["sentiment"] == 'NEU'].head(1))
display(df[df["sentiment"] == 'NEG'].head(1))
