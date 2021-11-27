# С помощью функции map выведите список имен с заглавной буквы.
# names = ['alfred', 'tabitha', 'william', 'arla']
# Результат: ['Alfred', 'Tabitha', 'William', 'Arla']
# Используйте функцию написанную через def, затем Лямбда-функцию, затем метод класса str.

names = ['alfred', 'tabitha', 'william', 'arla']

# First version
# def title(obj):
#     return obj.title()
#
#
# list1 = list(map(title, names))
# print(list1)

# Second version

list2 = list(map(lambda obj: obj.title(), names))
print(list2)
