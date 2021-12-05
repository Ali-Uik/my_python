# json, virtual environment библиотеки
from pprint import pprint
import json
import requests

json_data = []
# while True:
#     name = input('Введите имя: ')
#     if name.lower() == 'print':
#         pprint(json_data)
#         with open('json_data.json', mode='w', encoding='utf-8') as file:
#             json.dump(json_data, file, ensure_ascii=False)
#             # json.load() - что бы открыть json файл
#         break
#     lastname = input('Введите фамилию: ')
#     age = input('Введите возраст: ')
#     json_data.append({
#         'Имя': name,
#         'Фамилия': lastname,
#         'Возраст': age
#     })

# users = requests.get('https://jsonplaceholder.typicode.com/users').json()
# for user in users:
#     print(user['name'])

parameters = {
    'appid': 'd0c4c1e4babd454e692db213ba832310',
    'units': 'metric',
    'lang': 'ru'
}
