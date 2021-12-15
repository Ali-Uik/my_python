import json
from bs4 import BeautifulSoup

import requests

cat_list = ['social', 'army']
# cat_list = ['social', 'army', 'politics', 'business', 'comments', 'culture', 'science', 'tech', 'auto', 'style',
#             'photo', 'infographics', 'exclusive', 'about']

for i in cat_list:
    response = requests.get(f'https://www.gazeta.ru/{i}/').text
    soup = BeautifulSoup(response, 'html.parser')
    title = soup.find_all('div', class_='b_ear-title')
    title_text = title.find('a')['href']
    # description = soup.find_all('div', class_='b_ear-intro')
    # print(f'{i.upper()}', title, title_text)
    # print(f'{i.upper()}', description)
    # print(description)
    # print(soup)
    # with open('{i}.json', mode='w', encoding='uts=f-8') as file:
    #     json.dump()
