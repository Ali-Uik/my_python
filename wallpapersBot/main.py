from bs4 import BeautifulSoup
import requests
import os
from dotenv import load_dotenv
import re  # импорт регулярные выражения
import sqlite3

db = sqlite3.connect('wallpapers.db', check_same_thread=False)
cursor = db.cursor()
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

    def get_html(self, i):
        try:
            html = requests.get(self.url + f'/page{i}').text
            return html
        except Exception:
            print('Не удалось получить данные')

    def get_soup(self, i):
        html = self.get_html(i)
        soup = BeautifulSoup(html, 'html.parser')
        return soup

    def get_data(self):
        if self.name not in os.listdir():
            os.mkdir(str(self.name))
        # for i in range(1, self.page + 1):
        for i in range(1, 4):
            soup = self.get_soup(i)
            images_blocks = soup.find_all('a', class_='wallpapers__link')
            for block in images_blocks:
                page_link = HOST + block['href']
                # print(block)
                # print(page_link)
                page_html = requests.get(page_link).text
                page_soup = BeautifulSoup(page_html, 'html.parser')
                section = page_soup.find_all('span', class_='wallpaper-table__cell')[1].get_text(strip=True)
                # print(section)
                image_link = block.find('img', class_='wallpapers__image').get('src')
                image_link = image_link.replace('300x168', section)
                print(image_link)
                cursor.execute('''INSERT OR IGNORE INTO images(image_link,category_id) VALUES (?,?);''',
                               (image_link, self.category_id))
                db.commit()

                if self.download:
                    responseImage = requests.get(image_link).content
                    image_name = image_link.replace('https://images.wallpaperscraft.ru/image/single/', '')
                    with open(file=f'{self.name}/{image_name}.jpg', mode='wb') as file:
                        file.write(responseImage)


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
        pages = int(re.findall(r'[0-9][0-9]+', name)[0]) // 15
        print(pages)
        cursor.execute('''
            INSERT OR IGNORE INTO categories(category_name) VALUES (?);
        ''', (true_name,))
        # INSERT INTO categories(category_name) VALUES(?) ON CONFLICT DO NOTHING;
        # INSERT OR IGNORE INTO categories(category_name) VALUES(?) ;
        db.commit()
        print(f'Парсим категорию: {true_name}')
        cursor.execute('''
            SELECT category_id FROM categories WHERE category_name = ?;
        ''', (true_name,))
        category_id = cursor.fetchone()[0]
        print(f'category_id = {category_id}')
        parser = Category_parser(url=link,
                                 name=true_name,
                                 category_id=category_id,
                                 download=False)
        parser.get_data()


parsing()
