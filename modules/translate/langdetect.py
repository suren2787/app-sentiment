from deep_translator import batch_detection

def detect(textarray, apikey):
    langarray = batch_detection(textarray, api_key=apikey)
    return langarray

# texts = ['bonjour la vie', 'hello world']
# print(detect(texts)) # output: [fr, en]