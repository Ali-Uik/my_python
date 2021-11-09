# Условия и if else блоки
num1 = 15
num2 = 10
num3 = 20
num4 = 10

# < > <= >=
# print('num1 > num2', f'{num1} > {num2}', num1 > num2)
# print('num2 > num3', f'{num2} > {num3}', num2 > num3)

# Сравнение на равенство ==
# print('num2 == num4', f'{num2} == {num4}', num2 == num4)

# Сравнение на не равенство !=
# print('num2 != num4', f'{num2} != {num4}', num2 != num4)
# print('num2 != num3', f'{num2} != {num3}', num2 != num3)

# ctrl + shift + up/down - передвижение блоков/строк

# str1 = 'ab'
# str2 = 'abc'
# str3 = 'abCdef'
# print(str2 > str1)
# print(str3 > str2)

# Готовые методы работы строк
# str1 = 'Hello world'
# print(str1.lower())  # hello world
# print(str1.upper())  # HELLO WORLD
# print(str1.title())  # Hello World
# print(str1.capitalize())  # Hello world


# num = input('Введите цисло:')
# num_float = float(num)
# if num_float > 0:
#     print('Цисло явно больше нуля')
# elif num_float < 0:
#     print('Число меньше нуля')
# else:
#     print('Число точно равен нулю')


# num = input('Введите число:')
# num_float = float(num)
# x = num_float % 2
# if x == 1:
#     print('Вы ввели нечетное число')
# elif x == 0:
#     print('Вы ввели четное число')
# else:
#     print('Вы ввели дробное число')

# weather = input('Введите погоду своего города: ').lower()
#
# if weather == "холодно" or weather == "дождь":
#     print('Оденьтесь теплее')
# elif weather == "ясно" or weather == "облачно":
#     print('Можете гулять на улице')
# else:
#     print('Токого погоды не существует')


# num = input('Введите число:')
# num_float = float(num)
# x = num_float % 2
# print('Вы ввели четное число') if x == 0 else print('Вы ввели нечетное число')

# Администраторы
# Сансаныч 12345678     Женя StalinSuper

# Менеджеры
# Сергей 87654321      Толя qwerty


name = input('Введите имя: ').lower()
password = input('Введите пароль: ')
if not name and not password:
    print('Вы ничего не ввели')
elif not name:
    print('Вы не ввели логин')
elif not password:
    print('Вы не ввели пароль')
elif name == 'сансаныч' and password == '12345678' or name == 'женя' and password == 'StalinSuper':
    print(f'Здравствуйте уважаемый Амдинистратор {name.capitalize()}')
elif name == 'сергей' and password == '87654321' or name == 'толя' and password == 'qwerty':
    print(f'Здравствуйте уважаемый Менеджер {name.capitalize()}')
else:
    print('Ты такой? Давай до свидания.')
