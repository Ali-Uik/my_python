# функциональное программирование
# пуст есть список чисел в строке - надо переделать в список чисел


# nums = ['1', '2', '3']  # надо пулочит [1,2,3]
# intNums = []
# for i in nums:
#     intNums.append(int(i))

# print(nums)

# map(что сделать? , с кем сделать(список)) -> map

# nums3 = map(int, nums)


# print('list', intNums, intNums.__sizeof__())
#
# print('map', list(nums3), nums3.__sizeof__())


# def nadva(x):
#     l = x * 2
#     return l
#
#
list1 = [i for i in range(1, 11)]

# list2 = list(map(nadva, list1))
# print(list1)
# print(list2)
#
#
# def add_hello(obj):
#     return str(obj) + 'hello'
#
#
# list3 = list(map(add_hello, list1))
# print(list3)


# filters(функция фиьтрации, что фильтровать(список))
# def even(number):
#     return number % 2 == 0  # возврашаеть False или True
#
#
# list5 = list(filter(even, list1))
# print(list5)

# Lambda функции
# def get_str(number):
#     return str(number)
#
#
# list8 = list(map(get_str, list1))
# print(list8)
#
#
# def get_int(str1):
#     return int(str1)
#
#
# list9 = list(map(get_int, list8))
# print(list9)

# lambda <объект>:<что сделать>

# list10 = list(map(lambda x: str(x), list1))
# print(list10)

list2 = [i for i in range(10)]
list3 = [i for i in range(25, 36)]
print(list2, list3)
list4 = list(map(lambda x, y: x + y, list2, list3))
print(list4)
