from bs4 import BeautifulSoup
import requests
import os
from dotenv import load_dotenv
import re  # импорт регулярные выражения

load_dotenv()
URl = os.getenv('URL')
HOST = os.getenv('HOST')


class Category_parser:
    def __init__(self, url, name, category_id, page=3, download=False):
        self.url = url
        self.name = name
        self.category_id = category_id
        self.page = page
        self.download = download


def parsing():
    html = requests.get(URl).text
    soup = BeautifulSoup(html, 'html.parser')
    block = soup.find('ul', class_='filters__list')
    filters = block.find_all('a', class_='filter__link')
    for filter in filters:
        link = HOST + filter.get('href')
        print(link)
        name = filter.get_text(strip=True)
        print(name)
        true_name = re.findall(r'[3]*[a-zA-Zа-яА-Яё]+', name)[0]
        print(true_name)
        pages = int(re.findall(r'[0-9][0-9]+', name)[0])//15
        print(pages)


parsing()
