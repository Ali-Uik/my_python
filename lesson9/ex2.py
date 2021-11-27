# Написать 2 функции фильтрации по типу и создать 2 списка с помощью filter

musor = ['plan', 42, 'money', 21, 'help', 14]


def isInt(i):
    return type(i) is int


def isStr(i):
    return type(i) is str


intList = list(filter(isInt, musor))
strList = list(filter(isStr, musor))
print(intList)
print(strList)
