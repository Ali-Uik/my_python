months = ['', 'Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь',
          'Ноябрь', 'Декабрь']
while True:
    num = int(input('Введите число от 1 до 12: '))
    if num == 0:
        break
    elif 1 <= num <= 12:
        print(months[num])
    else:
        print('Неверное значение! ')
