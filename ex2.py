a = int(input('a-ni kiriting: '))
b = int(input('b-ni kiriting: '))
c = int(input('c-ni kiriting: '))

d = b ** 2 - 4 * a * c
if d < 0:
    print('Yechim yuq')
elif d == 0:
    x = -b / 2 * a
    print(f'Bitta yechimga ega: x = {x} ')
elif d > 0:
    x1 = (-b + d ** 1 / 2) / 2 * a
    x2 = (-b - d ** 1 / 2) / 2 * a
    print(f'Ikkita yechimga ega: x1 = {x1}, x2= {x2}')

