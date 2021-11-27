# С помощью функции filter и Лямбда-функции выведите список слов-палиндромов.
# words = ['Anna', 'Alexey', 'Alla', 'Kazak', 'Dom']
# Результат: ['Anna', 'Alla', 'Kazak']
words = ['Anna', 'Alexey', 'Alla', 'Kazak', 'Dom']

def palindrom(obj):
    if obj == obj[::-1]:
        return obj

print(palindrom(words))

# list2 = list(filter(palindrom, words))
# print(list2)

# list3 = list(map(lambda x: x == x[::-1], words))
# print(list3)
