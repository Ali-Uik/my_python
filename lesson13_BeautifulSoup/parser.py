import requests
from bs4 import BeautifulSoup
from pprint import pprint

URL = 'https://auto.ria.com/newauto/marka-jeep/'
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/94.0.4606.85 '
                  'YaBrowser/21.11.2.773 '
                  'Yowser/2.5 Safari/537.36',
    'accept': '*/*'}
HOST = 'https://auto.ria.com'


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('section', class_='proposition')
    cars = []
    for item in items:
        price = item.find('span', class_='green')
        if price:
            price = price.get_text(strip=True)
        else:
            price = 'Цена не определено'
        uah_price = item.find('span', class_='size16')
        if uah_price:
            uah_price = uah_price.get_text(strip=True)
        else:
            uah_price = 'Цена не определено'

        # location_text = location.get_text(strip=True)
        location = item.find('span', class_='item region')
        # location2 = location.get_text(strip=True)

        cars.append({
            'title': item.find('div', class_='proposition_title').get_text(strip=True),
            'link': HOST + item.find('a')['href'],
            'usd_price': price,
            'uah_price': uah_price,
            'location': location

        })
        print(location)
    pprint(cars)


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
    else:
        print('Error!')


parse()
