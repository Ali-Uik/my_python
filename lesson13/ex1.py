import requests
from bs4 import BeautifulSoup
from pprint import pprint

response = requests.get('https://www.themoscowtimes.com/').text
soup = BeautifulSoup(response, 'html.parser')
articles = soup.find_all('div', class_='article-excerpt-default')
# print(articles)
for article in articles:
    title = article.find('h3', class_='article-excerpt-default__headline').get_text(strip=True)
    print('TITLE:', title)
    descriprion = article.find('div', class_='article-excerpt-default__teaser').get_text(strip=True) if article.find(
        'div', class_='article-excerpt-default__teaser') else "Нет описания"
    print('DESCRIPTION:', descriprion)
    category = article.find('span', class_='label article-excerpt-default__label').get_text(strip=True) if article.find(
        'span', class_='label article-excerpt-default__label') else "No category"
    print('CATEGORY:', category)
