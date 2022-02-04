import json
from pprint import pprint
from bs4 import BeautifulSoup
import requests

response = requests.get('https://www.gazeta.ru/').text
soup = BeautifulSoup(response, 'html.parser')
# print(soup)
title = soup.find_all('div', class_='b_ear-title')
print(title)
