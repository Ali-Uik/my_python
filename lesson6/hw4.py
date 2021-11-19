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
