# С помощью функции filter выведите список оценок, которые больше 75.
# scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# Результат: [90, 76, 88, 81]
# Сначала используйте функцию, объявленную с помощью def, а затем воспользуйтесь Лямбда-функцией.

scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]


# def version
def func(num):
    return num > 75


list1 = list(filter(func, scores))
print(list1)

# lambda version


list2 = list(filter(lambda obj: obj > 75, scores))
print(list2)
