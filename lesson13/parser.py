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

        # cars.append({
        #     'title': item.find('div', class_='proposition_title').get_text(strip=True),
        #     'link': HOST + item.find('a')['href'],
        #     'usd_price': item.find('span', class_='size16').get_text(strip=True),
        #
        # })
    pprint(price.get_text(strip=True))



def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
    else:
        print('Error!')


parse()
