a = input('Введи: ')
b = a.split('+')
summa = 0
for i in b:
    summa = summa + int(i)
print(summa)
