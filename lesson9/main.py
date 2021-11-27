# функциональное программирование
# пуст есть список чисел в строке - надо переделать в список чисел


nums = ['1', '2', '3']  # надо пулочит [1,2,3]
intNums = []
for i in nums:
    intNums.append(int(i))

# print(nums)

# map(что сделать? , с кем сделать(список)) -> map

nums3 = map(int, nums)


# print('list', intNums, intNums.__sizeof__())
#
# print('map', list(nums3), nums3.__sizeof__())


def nadva(x):
    l = x * 2
    return l


list1 = [i for i in range(1, 11)]
list2 = list(map(nadva, list1))
print(list1)
print(list2)


def add_hello(obj):
    return str(obj) + 'hello'


list3 = list(map(add_hello, list1))
print(list3)


