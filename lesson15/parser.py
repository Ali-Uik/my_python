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
        for category in category_links:
            category_title = category.find('h2', class_='content__title').get_text(strip=True)
            print(category_title)
            self.DATA[category_title] = []
            link = HOST + category.get('href')
            print(link)
            category_page = self.get_html(link)
            self.smartphones_page_parser(category_page, category_title)

    def smartphones_page_parser(self, category_page, category_title):
        """Парсим каждую страницу с телефонами"""
        soup = BeautifulSoup(category_page, 'html.parser')
        section = soup.find('div', class_='product-list__wrap')
        products = section.find_all('div', class_='product-list__item')
        for product in products[:MAX_QUANTITY]:
            product_name = product.find('a', class_='product-name').get_text(strip=True)
            print(product_name)


def start_category_parsing():
    parser = CategoryParser()
    print('Парсер начал работу')
    start = time.time()
    html = parser.get_html('https://texnomart.uz/mobile/katalog/telefony')
    parser.category_parser(html)
    finish = time.time()
    work_time = round(finish - start, 2)
    print(f'Парсер отработал за {work_time} секунд')


start_category_parsing()
