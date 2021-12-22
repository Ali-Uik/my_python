import requests
from bs4 import BeautifulSoup
import time
from configs import *
from base_parser import BaseParser


class CategoryParser(BaseParser):  # 5
    def __init__(self):
        super(CategoryParser, self).__init__()  # 6 Запуск конструктора родителя
        self.DATA = {}  # 7

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


def start_category_parsing():  # 8
    parser = CategoryParser()  # 9
    print('Парсер начал работу')  # 10
    # print(parser)
    start = time.time()  # 11
    html = parser.get_html('https://texnomart.uz/mobile/katalog/telefony')
    # print(html)
    parser.category_parser(html)
    finish = time.time()  # 12
    work_time = round(finish - start, 2)  # 13
    print(f'Парсер отработал за {work_time} секунд')  # 14


start_category_parsing()
