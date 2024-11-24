import json
import time
from pathlib import Path
import os
import pandas as pd
import matplotlib.pyplot as plt

play_store_summary_file = 'results/ps-summary.json'
comments=[]

#Open file and filter only comments
with open(play_store_summary_file, 'r') as ifh:
    reviews = json.load(ifh)

   
# Load the data in a dataframe
df = pd.DataFrame(reviews)
pd.set_option('display.max_colwidth', None)

sentiment_counts = df.groupby(['sentiment']).size()
print(sentiment_counts)

# Let's visualize the sentiments
fig = plt.figure(figsize=(6,6), dpi=100)
ax = plt.subplot(111)
figure = sentiment_counts.plot.pie(ax=ax, autopct='%1.1f%%', startangle=270, fontsize=12, label="")
plt.title("PIE CHART")
plt.savefig('results/diagrams/piechart.png')


from wordcloud import WordCloud
from wordcloud import STOPWORDS
  
# Wordcloud with positive tweets
positive_tweets = df['content'][df["sentiment"] == 'POSITIVE']
stop_words = ["https", "co", "RT"] + list(STOPWORDS)
positive_wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white", stopwords = stop_words).generate(str(positive_tweets))
plt.figure()
plt.title("Positive comments - Wordcloud")
plt.imshow(positive_wordcloud, interpolation="bilinear")
plt.axis("off")
plt.savefig('results/diagrams/positivecomments')
 
# Wordcloud with negative tweets
negative_tweets = df['content'][df["sentiment"] == 'NEGATIVE']
stop_words = ["https", "co", "RT"] + list(STOPWORDS)
negative_wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white", stopwords = stop_words).generate(str(negative_tweets))
plt.figure()
plt.title("Negative comments - Wordcloud")
plt.imshow(negative_wordcloud, interpolation="bilinear")
plt.axis("off")
plt.savefig('results/diagrams/negativecomments')