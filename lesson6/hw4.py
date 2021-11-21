# Даны два списка одинаковой длины. Необходимо создать из них словарь таким образом, чтобы элементы первого списка были
# ключами, а элементы второго — соответственно значениями нашего словаря.

numList = [i for i in range(5)]
strList = ['Ali', 'Bonu', 'Sabrina', 'Zara', 'Dinara']
lennumList = len(numList)
lenstrList = len(strList)
if lenstrList == lenstrList:
    for item in range(lennumList):
        dic = {
            numList[item]: strList[item]
        }
        print(dic)
else:
    print('Эррор')

# Вариант учителя
# list1 = [i for i in range(10)]
# list2 = [i for i in range(10)]
# dict2 = {}
# for i in range(len(list1)):
#     dict2[list1[i]] = list2[i]*2
# print(dict2)
