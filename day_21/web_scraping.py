import requests
from bs4 import BeautifulSoup
import json

url = "http://www.bu.edu/president/boston-university-facts-stats/"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

data = {
    "title": soup.title.text,
    "content": soup.body.get_text(separator="\n", strip=True)
}

with open("bu_data.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4)

print("JSON file created successfully.")