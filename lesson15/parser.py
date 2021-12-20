import requests
from bs4 import BeautifulSoup
import time
from configs import *
from base_parser import BaseParser


class CategoryParser(BaseParser):
    def __init__(self):
        super(CategoryParser, self).__init__()
        self.DATA = {}

    def category_parser(self, html):
        """Парсим все блоки из страницы категорий"""
        soup = BeautifulSoup(html, 'html.parser')
        category_links = soup.find_all('a', class_='category__link')


def start_category_parsing():
    parser = CategoryParser()
    print('Парсер начал работу')
    start = time.time()
    html = parser.get_html('https://texnomart.uz/mobile/katalog/telefony')

    finish = time.time()
    work_time = round(finish - start, 2)
    print(f'Парсер отработал за {work_time} секунд')


start_category_parsing()
