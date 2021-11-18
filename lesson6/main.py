# Словари (ключ и значение)
# Как создаь словарь
# dict1 = {}
# dict2 = dict()

# Самым простым примером словаря для понимания - Контакты
# name = 'Nodir'
# contacts = {
#     # ключ: Значение
#     'Ali': '+998975103870',
#     'Bonu': 998935093870,
#     102: 'Милиция',
#     name: 'Bu Nodir',
#     'Hello нооборот': 'Hello'
# }
# print(contacts)
# print(contacts['Bonu'])  # Вытаскиваем определенное значение
# contacts['скорая'] = 103  # Добавление элемента
# print(contacts)

# del contacts['скорая']   # удаление элемента
# print(contacts)

# for item in contacts:  # он вам выплюнет только ключи - не рекомендовано
#     print(item)
# contacts = {
#     'Ali': +998975103870,
#     'Bonu': +998935093870,
#     'Onam': +998977914863,
#     'Uy': +998883777388
# }
# for item in contacts.keys():  # обходит по ключам
#     print(item, ':', contacts[item])
# for value in contacts.values():
#     print(value)

# Как брать сразу два значение
# for key, value in contacts.items():
#     print(key, ':', value)

# list1 = [i for i in range(10)]
# numbers = {}
# for i in list1:
#     numbers[i] = i ** 2
# print(numbers)

# Копирование словаря
# contacts2 = contacts.copy()

# копирование в цикле
# мой вариант
# contacts3 = {}
# for key in contacts:
#     contacts3[key] = contacts[key]
# print(contacts3)

# вариант учителя
# contacts3 = {}
# for key, value in contacts.items():
#     contacts3[key] = value
# print(contacts)
# print(contacts3)

# Генератор словарей
# numbers2 = {x: x ** 2 for x in range(10)}
# print(numbers2)
# contacts4 = {x: y for x, y in contacts.items()}
# print(contacts4)
# names = ['Ali', 'Bonu', 'Sabrina', 'Zara', 'Dinara']
# marks = {key: [value for value in range(10)] for key in names}
# print(marks)

# Очистит словарь полностью
# marks.clear()
# print(marks)
# Вложенность
# списки словарей
# список пользователей
# userList = [{'id': i, 'name': 'Lyuk'} for i in range(10)]
# print(userList)
# print(userList[5]['name'])

# безконечно вбиваем по отдельности Имя, фамилия, возраст(int), город, дом
# если в имя напишетe 'stop' то программа остановится и вернет список пользователей - список словарей
# при этом в словаре должен быть 'adress':{'city':...,'house':....}

from pprint import pprint
contactsList = []
while True:
    name = input('Введите имя: ')
    if name == 'stop':
        pprint(contactsList)
        break
    l_name = input('Введите фамилия: ')
    age = int(input('Введите возраст: '))
    city = input('Введите город: ')
    house = input('Введите дом: ')
    contactsList.append({
        'Имя': name,
        'Фамилия': l_name,
        'Возраст': age,
        'Адресс': {
            'Город': city,
            'Дом': house
        }
    })
