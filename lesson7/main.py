# Функции
# Задача, которая выполняется по вызову и не зависит от объекта
# Функции создаются словом def <название>():
# def HelloUser():
#     print("Привет пользователь")
#
#
# HelloUser()

# В функцию можно подовать аргументы len(list)
#
# def HelloName(name):
#     print(f"Hello {name}")
#
#
# HelloName('Izzat')

# def calculator(a, b):
#     # Функции умеют возвращать значения
#     return a + b
#
#
# print(calculator(10, 20))

# Получение данных и вывод списка

# def calculator(a, b):
#     return a + b, a - b, a * b, a / b
#
#
# print(calculator(5, 4))

# def calculator(a, b, operation='**'):  # Значение по умалчанию
#     if operation == '+':
#         return a + b
#     elif operation == '-':
#         return a - b
#     elif operation == '*':
#         return a * b
#     elif operation == '/':
#         return a / b
#     elif operation == '**':
#         return a ** b


#
#
# while True:
#     a = float(input('Введите число: '))
#     b = float(input('Введите число: '))
#     operation = input('Введите операцию: ')
#     if operation == 'stop':
#         print('Вы остонавили операцию')
#         break
#     print(calculator(a, b, operation))
#     print(calculator(a, b))

# Позиционка
def calculator(a=5, b=5, operation='**'):  # Значение по умалчанию
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        if b == 0:
            print(f'b не должен ровним к нулю')
        else:
            return a / b
    elif operation == '**':
        return a ** b


c = calculator(operation='+', a=5, b=6)
print(c)
