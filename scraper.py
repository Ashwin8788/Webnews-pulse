import requests
from bs4 import BeautifulSoup

def get_news():
    url = "https://timesofindia.indiatimes.com/rssfeedstopstories.cms"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "xml")

    items = soup.find_all("item")

    news_list = []

    for item in items[:10]:
        title = item.find("title").text if item.find("title") else "No Title"
        link = item.find("link").text if item.find("link") else "No Link"
        description = item.find("description").text if item.find("description") else "No Description"

        news_list.append({
            "title": title,
            "link": link,
            "description": description
        })

    return news_list