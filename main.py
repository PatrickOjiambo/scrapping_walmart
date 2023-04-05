from requests_html import HTMLSession
from bs4 import BeautifulSoup
import requests

url = "https://www.walmart.com/"
page = requests.get(url)

soup = BeautifulSoup(page.content, "lxml")
print(soup)

# Print product name
