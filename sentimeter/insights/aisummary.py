import google.generativeai as genai

genai.configure(api_key="AIzaSyAddiknaRgX_43CkjyiowT1cO_dbTcWqwU")
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Explain how AI works")
print(response.text)