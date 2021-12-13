import json
from bs4 import BeautifulSoup

import requests

cat_list = ['social', 'army', 'politics', 'business', 'comments', 'culture', 'science', 'tech', 'auto', 'style',
            'photo', 'infographics', 'exclusive', 'about']

for i in cat_list:
    response = requests.get(f'https://www.gazeta.ru/{i}/').text
    soup = BeautifulSoup(response, 'html.parser')
    title = soup.find('div', class_='b_ear-title')
    print(title)
    # print(soup)
    # with open('{i}.json', mode='w', encoding='uts=f-8') as file:
    #     json.dump()
