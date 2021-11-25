# ppp = []  # 1
#
#
# def calc(*args):
#     num = int(input('enter num to calculate: '))
#
#     for i in str(num):
#         ppp.append(int(i))
#
#     return (sum(ppp))
#
#
# print(calc())

a = int(input('enter seconds to convert: '))  # 2 надо причесать что бы вывод был красивым

rez = []

days = a // 86400

rez.append(days)

hours = (a % 86400) // 3600

rez.append(hours)

mins = a % 86400 % 3600 // 60

rez.append(mins)

sec = a % 86400 % 3600 % 60

rez.append(sec)

print(rez)
