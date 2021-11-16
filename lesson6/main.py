# Словари (ключ и значение)
# Как создаь словарь
dict1 = {}
dict2 = dict()

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
contacts = {
    'Ali': +998975103870,
    'Bonu': +998935093870,
    'Onam': +998977914863,
    'Uy': +998883777388
}
# for item in contacts.keys():  # обходит по ключам
#     print(item, ':', contacts[item])
# for value in contacts.values():
#     print(value)

# Как брать сразу два значение
# for key, value in contacts.items():
#     print(key, ':', value)

list1 = [i for i in range(10)]
numbers = {}
for i in list1:
    numbers[i] = i ** 2
print(numbers)
