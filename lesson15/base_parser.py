import requests
import json
from configs import *


class BaseParser:
    def __init__(self):
        self.URL = URL
        self.HOST = HOST

    def get_html(self, url):
        """Получение страницы сайта"""
        response = requests.get(url)
        try:
            response.raise_for_status()  # Узнаем статус запроса
            return response.text  # Возврат страницы
        except requests.HTTPError:
            print(f'Проищошло ошибка {response.status_code}')

    @staticmethod
    def save_data_to_json(file_path, data):
        """Сохранение данных в json"""
        with open(f'{file_path}.json', mode='w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    @staticmethod
    def save_data_to_htmk(file_path, data):
        """Сохранение данных в html"""
        with open(f'{file_path}.html', mode='w', encoding='utf-8') as file:
            file.write(str(data))
