import requests
from bs4 import BeautifulSoup
import datetime

def scrape_headlines():
    base_url = "https://news.ycombinator.com/"
    today = datetime.date.today()
    try:
        response = requests.get(base_url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
    except requests.exceptions.RequestException as e:
        print("request error:", e)
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

def generate_numbered_list(data):
    numbered_list = ""
    for i, item in enumerate(data, start=1):
        numbered_list += f"{i}. {item['title']}\n"
    return numbered_list
    

def measure_length(item):
    return len(item["title"])

def get_top_titles_by_length(data, n=2):
    top_titles_by_length = sorted(data, key=measure_length, reverse=True)
    return top_titles_by_length[:n]

def count_items(data):
    total_items = len(data)
    return total_items

def write_report(output_file_path, numbered_list, top_titles_by_length, total_items):
    with open(output_file_path, "w") as f:
        f.write("TOTAL ITEMS\n\n")
        f.write("-------------\n")
        f.write(f"{total_items}\n\n")
        f.write("LIST\n\n")
        f.write("-------------\n")
        f.write(f"{numbered_list}\n\n")
        f.write(f"TOP {len(top_titles_by_length)} LONGEST TITLES\n\n")
        f.write("-------------\n")
        for item in top_titles_by_length:
            f.write(f"- {item['title']}\n")
        f.write("\n")


def main():
    output_file_path = "report .txt"
    data = scrape_headlines()
    if data is None:
        return
    numbered_list = generate_numbered_list(data)
    top_titles_by_length = get_top_titles_by_length(data)
    total_items = count_items(data)
    write_report(output_file_path, numbered_list, top_titles_by_length, total_items)


if __name__ == "__main__":
    main()


