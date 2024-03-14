import requests
from send_email import send_email

api_key = "7830a4cdc4c347889873862ea617a2dc"
# url = "https://newsapi.org/v2/everything?q=tesla&from=2024-02-13&sortBy=publishedAt&apiKey=7830a4cdc4c347889873862ea617a2dc"
url = ("https://newsapi.org/v2/top-headlines?"
       "country=us&category=business&"
       "apiKey=7830a4cdc4c347889873862ea617a2dc&"
       "language=en")

request = requests.get(url)
content = request.json()

body="Subject: Today news"+ "\n"

for article in content["articles"][:20]:
    
    title = article["title"]
    description = article["description"]
    if description is not None:
        body = body + title + "\n" + description +"\n" + article["url"] +"\n\n"

    # body = body + str(article["title"]) + "\n" + str(article["description"]) + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)