import google.generativeai as genai
genai.configure(api_key="AIzaSyBgKyZ1SL4mbXHsLdclD7dNfNVZXmSBm-E")
model = genai.GenerativeModel("gemini-pro")
response = model.generate_content("What is the meaning of life?")
print(response.text)