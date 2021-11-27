# написать функцию, которая принимает элемент и если он число делат +10
# если это строка пуст - + 'python'
# пройтис  map по списку и прогнать эту функцию
# a = input('Введите: ')
#
#
# def aInt(a):
#     return a + 10
#
#
# def aStr(a):
#     return a + 'Python'
#
#
# intList = []
# strList = []
#
# if type(a) == int:
#     intList.append(list(map(aInt, a)))
#     print(intList)
# elif type(a) == str:
#     strList.append(list(map(aStr, a)))
#     print(strList)


musor = ['plan', 42, 'money', 21, 'help', 14]


def choose(obj):
    if type(obj) == int:
        return obj + 10
    elif type(obj) == str:
        return obj + ' Python'


list1 = list(map(choose, musor))
print(list1)
