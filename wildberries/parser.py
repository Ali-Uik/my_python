from base_parser import BaseParser
from bs4 import BeautifulSoup
from time import time
import requests
from configs import *


class ParserCategory(BaseParser):
    def __init__(self):
        super(ParserCategory, self).__init__()

    def category_parser(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        section = soup.find('div', class_='menu-burger__main')
        category_title = section.find_all('a', class_='menu-burger__main-list-link')
        print(f'{category_title}\n')


def start_parsing():
    parsing = ParserCategory()
    html = parsing.get_html('https://www.wildberries.ru')
    parsing.category_parser(html)


start_parsing()
