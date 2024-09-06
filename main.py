import requests

API_key = "6dc544e9c0f348e380ebe7612475cec7"
url = ("https://newsapi.org/v2/everything?q=tesla&from=2024-08-06&sortBy="
       "publishedAt&apiKey=6dc544e9c0f348e380ebe7612475cec7")

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access data
for article in content["articles"]:
    print(article["title"])


