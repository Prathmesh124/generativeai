import google.generativeai as genai
genai.configure(api_key="AIzaSyBgKyZ1SL4mbXHsLdclD7dNfNVZXmSBm-E")
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat()
while True:
    message = input("You: ")
    response = chat.send_message(message)
    print("Gemini: " + response.text)