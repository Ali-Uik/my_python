# С помощью функции filter и Лямбда-функции выведите список слов-палиндромов.
# words = ['Anna', 'Alexey', 'Alla', 'Kazak', 'Dom']
# Результат: ['Anna', 'Alla', 'Kazak']
words = ['Anna', 'Alexey', 'Alla', 'Kazak', 'Dom']


# version 1
def palindrom(a):
    return a.lower() == a[::-1].lower()


list1 = list(filter(palindrom, words))
print(list1)

# version 2
list3 = list(filter(lambda x: x.lower() == x[::-1].lower(), words))
print(list3)
