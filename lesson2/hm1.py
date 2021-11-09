a = int(input('Первое: '))
b = int(input('Второе: '))
c = int(input('Третья: '))

if a < b < c or c < b < a:
    print(f'Средное число:{b}')
elif b < a < c or c < a < b:
    print(f'Средное число:{a}')
elif a < c < b or b < c < a:
    print(f'Средное число:{c}')
