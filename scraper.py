import requests
from bs4 import BeautifulSoup

def scrape_headlines():
    base_url = "https://news.ycombinator.com/"
    try:
        response = requests.get(base_url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
    except requests.exceptions.RequestException as e:
        print("Request error:", e)
        return
    
    links = soup.find_all("span", class_="titleline")
    data = []
    for link in links:
        title = link.find("a")
        link_url = title["href"]
        item = {
            "title":title.text,
            "url": link_url
        }
        data.append(item)
    return data