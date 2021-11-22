# С помощью функции извлеките из списка числа, делимые на 15.
nums = [45, 55, 60, 37, 100, 105, 220]


def anyList(someList, givenIneger):
    return [i for i in someList if i % givenIneger == 0]


intList = anyList(nums, 15)

print(intList)
