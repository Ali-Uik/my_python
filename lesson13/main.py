import requests
from bs4 import BeautifulSoup
import json
from pprint import pprint

response = requests.get('https://www.themoscowtimes.com/').text

# print(response)

soup = BeautifulSoup(response, 'html.parser')
# print(soup)
# find - найдет первое совпадение
covid_section = soup.find('section', class_='covid19-ticker')
# print(covid_section)
# найдет все совпадения - и вернет список
blocks = covid_section.find_all('div', class_='block')
# print(blocks)
json_data = []
for block in blocks:
    digit = block.find('span', class_='digit')
    label = block.find('span', class_='label')
    # print(digit, label)
    if digit and label:
        digit = digit.get_text()  # вытаскивает текст
        label = label.get_text()
        # print(label, digit)
        json_data.append(
            {
                label: digit
            }
        )
# print(json_data)

with open('covid.txt', mode='w', encoding='utf-8') as file:
    json.dump(json_data, file, indent=4, ensure_ascii=False)
