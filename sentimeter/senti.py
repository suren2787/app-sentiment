from transformers import pipeline
sentiment_pipeline = pipeline("text-classification",model='bhadresh-savani/distilbert-base-uncased-emotion')
data = ["I love you", "I hate you"]
result = sentiment_pipeline(data)
print(result)

# from transformers import pipeline
# classifier = pipeline("text-classification",model='bhadresh-savani/distilbert-base-uncased-emotion', return_all_scores=True)
# prediction = classifier("I love using transformers. The best part is wide range of support and its easy to use", )
# print(prediction)