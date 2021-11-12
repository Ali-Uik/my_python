# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for i in list:
#     print('Hello')  # печатает 10 раз  Hello

# range(start=0, finish, step=1)
#
# for i in range(10):
#     print(i)
#
# for i in range(3, 10):
#     print(i)

# list1 = []
# for i in range(100, 0, -2):
#     list1.append(i)
# print(list1)

# list2 = []
# for i in range(10):
#     list2.append(i ** 2)
# print(list2)

# Генераторы списков
# nums = [i for i in range(10)]
# strs = ['Hello' for i in range(10)]
# print(nums)
# print(strs)

# letters = [i for i in 'hello world']
# print(letters)

# array = [i for i in range(3)]
# array = [[j for j in range(3)] for i in range(3)]
# print(array)
# первый вариант
# num1 = [i for i in range(0, 100, 2)]
# num2 = [i for i in range(1, 100, 2)]
# print(num1)
# print(num2)
# второй вариант
# numbers = [[j for j in range(i, 100, 2)] for i in range(0, 2)]
# print(numbers)

# Генераторы с условиями

# odd = [i for i in range(100) if i % 2 != 0]
# even = [i for i in range(100) if i % 2 == 0]
# print(odd)
# print(even)

# list1 = [1, 2, 3, "car", "money", "boy"]
# intlist = [i for i in list1 if type(i) == int]
# strlist = [i for i in list1 if type(i) is str]
# print(intlist)
# print(strlist)

# max min sum

list1 = [1, 2, 3, 5, 9, 4, 7, 5, 3, 2, 8, 150]
# maximum = 0
# for i in list1:
#     if i > maximum:
#         maximum = i
# print('maximus:', maximum)
#
# minimum = maximum
# for i in list1:
#     if i < minimum:
#         minimum = i
# print('minimum:', minimum)

# sum
# sum = 0
# for i in list1:
#     sum = sum + i    # sum += i
# print(sum)
# есть и готовые функции
# print(max(list1))
# print(min(list1))
# print(sum(list1))

# Срезы списков
list1 = [i for i in range(20)]


# срезы [start = 0: finish = len(list)-1: step = 1]
print(list1[5:]) #[5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
print(list1[:10])
print(list1[5:10])
print(list1[5:10:2])
