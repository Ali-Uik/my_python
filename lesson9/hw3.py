# С помощью функции filter и Лямбда-функции выведите список слов-палиндромов.
# words = ['Anna', 'Alexey', 'Alla', 'Kazak', 'Dom']
# Результат: ['Anna', 'Alla', 'Kazak']
words = ['Anna', 'Alexey', 'Alla', 'Kazak', 'Dom']


def palindrom(a):
    for i in a:
        if i == i[::-1]:
            return i


print(palindrom(words))
# list1 = list(filter(palindrom, words))
# print(list1)

# print(palindrom("aziza"))

# list2 = list(filter(palindrom, words))
# print(list2)

# list3 = list(map(lambda x: x == x[::-1], words))
# print(list3)
