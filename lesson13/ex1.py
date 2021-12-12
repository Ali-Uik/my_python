import json

import requests
from bs4 import BeautifulSoup
from pprint import pprint

response = requests.get('https://www.themoscowtimes.com/').text
soup = BeautifulSoup(response, 'html.parser')
articles = soup.find_all('div', class_='article-excerpt-default')
# print(articles)
json_data = []
for article in articles:
    title = article.find('h3', class_='article-excerpt-default__headline').get_text(strip=True)
    print('TITLE:', title)
    descriprion = article.find('div', class_='article-excerpt-default__teaser').get_text(strip=True) if article.find(
        'div', class_='article-excerpt-default__teaser') else "Нет описания"
    print('DESCRIPTION:', descriprion)
    category = article.find('span', class_='label').get_text(strip=True) if article.find(
        'span', class_='label') else "No category"
    print('CATEGORY:', category)
    image_link = article.find('img')['src']
    print('IMAGE_LINK:', image_link)
    article_link = article.find('a')['href']
    print('ARTICLE_LINK:', article_link)
    # response2 = requests.get(article_link).text
    # soup2 = BeautifulSoup(response2, 'html.parser')
    json_data.append(
        {
            'TITLE': title,
            'DESCRIPTION': descriprion,
            'CATEGORY': category,
            'IMAGE LINK': image_link,
            'ARTICLE LINK': article_link
        }
    )
with open('news.json', mode='w', encoding='utf-8') as file:
    json.dump(json_data, file, indent=4, ensure_ascii=False)
