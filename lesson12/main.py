# json, virtual environment библиотеки
from pprint import pprint

json_data = []
while True:
    name = input('Введите имя: ')
    if name.lower() == 'print':
        pprint(json_data)
        break
    lastname = input('Введите фамилию: ')
    age = input('Введите возраст: ')
    json_data.append({
        'Имя': name,
        'Фамилия': lastname,
        'Возраст': age
    })
