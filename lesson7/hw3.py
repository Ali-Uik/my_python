# С помощью функции извлеките из списка числа, делимые на 15.
nums = [45, 55, 60, 37, 100, 105, 220]


def anyList(someList, givenType):
    return [i for i in someList if type(i) is givenType]


list1 = [1, 2, 3, 'a', 'b', 'c']
intList = clearList(list1, int)
strList = clearList(list1, str)
print(intList)
print(strList)

