import requests
from bs4 import BeautifulSoup

URL = 'https://auto.ria.com/newauto/marka-jeep/'
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/94.0.4606.85 '
                  'YaBrowser/21.11.2.773 '
                  'Yowser/2.5 Safari/537.36',
    'accept': '*/*'}


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('section', class_='proposition')
    cars = []
    for item in items:
        cars.append({
            'title': item.find('h3', class_='proposition_name').get_text(),

        })
    print(cars)


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
    else:
        print('Error!')


parse()
