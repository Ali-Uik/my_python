a = int(input('Первое: '))
b = int(input('Второе: '))
c = int(input('Третья: '))

if a == b and b == c and c == a:
    print('Количество совпадающих чисел: 3')
elif a == b or b == c or c == a:
    print('Количество совпадающих чисел: 2')
else:
    print('Совпадение нету между чисел')
