# функция print() Создано, чтобы печатать консоль

# print(10)  # int
# print(7.5)  # float
# print('Hello')  # string
# print("Hello")  # string
# print("пушкин сказал: 'привет'")  # string
#
# print(True)  # boolean
# print(False)  # boolean


# Матемачиские операции
# ctrl + D
# print(10 + 2)  # int
# print(10 - 2)  # int
# print(10 * 2)  # int
# print(10 / 2)  # float деление всегде берет float

# челочисленное деление
# print(18 // 2)
# print(9 // 2)

# Вывод остатка от деления
# print(10 % 2)
# print(9 % 2)

# ctrl + alt + l Форматирование кода по стандарту PEP8

# Возведение в степень
# print(2 ** 2)
# print(3 ** 2)

# Работа со строками
# print('Hello' + 'World')
# print('Hello ' + 'World')
# print('Hello' + ' World')
# print('Hello' + ' ' + 'World')  # самый правильный способ
# print('hello ' * 10)  # вернет 10 раз hello

# number = 10
# name = 'Ali'
# print(number)
# print(name)
# функция input() это- ввод в консоль


name = input('Введите ваше имя:')
lastname = input('Введите вашу фамилию:')
year = int(input('Введите  ваш год рождения:'))

today = 2021
age = today - year
age_str = str(age)
# print('Здравствуйте' + ' ' + name + ' ' + lastname + '.Вам ' + age_str + ' года')

#f строка
# print(f'Привет {name} {lastname}.Тебе {age_str} года')
# print(f'Привет {name} {lastname}.Тебе\n {age_str} года')
print(f'''Привет!!!
{name} {lastname}.
Тебе {age} лет''')
