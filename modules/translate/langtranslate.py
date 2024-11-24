from deep_translator import GoogleTranslator

def translate(sourcelang, targetlang, textarray):
    translated = GoogleTranslator(source=sourcelang, target=targetlang).translate_batch(textarray)
    return translated

# texts = ["hallo welt", "guten morgen"]
# print(translate(sourcelang="auto", targetlang="en", textarray=texts))