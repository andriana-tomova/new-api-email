import os

import requests
from dotenv import load_dotenv
from send_email import send_email

load_dotenv()
API_TOKEN = os.getenv("ACCESS_API_TOKEN")
topic = "tesla"

url = "https://newsapi.org/v2/everything?"\
      f"q={topic}"\
      "&from=2024-08-06&sortBy="\
      "publishedAt&"\
      f"apiKey={API_TOKEN}"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access data

body = "Subject: news" + "\n"
for article in content["articles"][:20]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" \
        + article["url"] + 2*"\n"

body = body.encode("utf-8")
# Send email
send_email(body)

