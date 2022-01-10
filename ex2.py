a = int(input('a-ni kiriting: '))
b = int(input('b-ni kiriting: '))
c = int(input('c-ni kiriting: '))
if a == 0 and b == 0 and c == 0:
    print('Cheksiz kop yechimga ega')
elif a == 0 and b != 0:
    print(f'Bitta yechimga ega:x = {-c / b}')
elif a == 0 and b != 0 and c == 0:
    print(f'x=0')
elif a == 0 and b == 0 and c != 0:
    print('Yechim yoq')
elif a != 0:
    d = b ** 2 - 4 * a * c
    if d < 0:
        print('Yechim yuq')
    elif d == 0:
        x = -b / 2 * a
        print(f'Bitta yechimga ega: x = {x} ')
    else:
        x1 = (-b + d ** 1 / 2) / 2 * a
        x2 = (-b - d ** 1 / 2) / 2 * a
        print(f'Ikkita yechimga ega: x1 = {x1}, x2= {x2}')

# a = [i for i in range(101)]
# print(a)
# tub_sonlar = []
# k = 0
# for i in a:
#     for j in i:
#
#
#
# print(tub_sonlar)
