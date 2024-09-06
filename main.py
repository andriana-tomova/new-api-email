import os

import requests
from dotenv import load_dotenv
from send_email import send_email

load_dotenv()
API_TOKEN = os.getenv("ACCESS_API_TOKEN")

url = ("https://newsapi.org/v2/everything?q=tesla&from=2024-08-06&sortBy="
       "publishedAt&apiKey=" + API_TOKEN)

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access data
body =""
for article in content["articles"]:
    body = body + article["title"] + "\n"

body = body.encode("utf-8")
# Send email
send_email(body)

