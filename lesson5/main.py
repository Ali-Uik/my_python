# break continue
# list1 = [i for i in range(100)]
# for i in list1:
#     print(i, 'Какая должно быть итерация')
#     if i % 2 == 0:
#         continue
#     print(i, 'Что мы получили в итоге')

# цикл по условию - while
# i = 0
# while i < 10:  # пока i<10 делай что-то
#     print(i)
#     i = i + 1

# i++ - инкремент
# i-- - декримент

# БЕЗКОНЕЧНЫЙ ЦИКЛ
# i = 0
# while True:  # пока правда - пока программа работает
#     print(i)
#     i += 1
#     if i == 100:
#         break

# Регистрация пользователей
# ТЗ - программа должно бесконечно спрашивать логин и пароль
# логин должен быть только из букс
# пароль не должен быть только из букв или только из цифр
# длина пароля должна быть более 8 символов
# Еслм все верно - записать в список нового пользователя
# Если введена секретная команда stop program - остановить программу
# и вывести весь список пользователей
# data_base = []
# while True:
#     login = input('Введите ваш логин: ')
#     if not login or not login.isalpha():  # isalpha() - метод строки
#         # True - если там все символы буквенные
#         # False- если нет букв
#         print('Не верно введен логин!')
#         continue
#     password = input('Введите пароль: ')
#     if login.lower() == 'stop' and password.lower() == 'program':
#         print(data_base)
#         break
#
#     if password.isalpha() or password.isdigit() or len(password) < 5:
#         print('Введен не верный формат пароля')
#         continue
#
#     data_base.append((login, password))

# Представим что вы владелец магазина
# Написать программу которая добавляет товар в список товаров при команде add<product_name>
# Удаляет продукт из списка при команде delete <product_name>
# input должен быть один

# Мой вариант
# products = ['milk', 'bread', 'doll']
# while True:
#     prod = input('введите имя товара: ')
#     prod_split = prod.split('-')
#     if prod_split[0] == 'stop':
#         print(products)
#         break
#     elif prod_split[0] == 'add':
#         products.append(prod_split[1])
#         continue
#     elif prod_split[0] == 'del':
#         products.remove(prod_split[1])
#         continue
#     else:
#         print('Вы не ввели не одного продукта')
#         continue


# Вариант учителья
products = ['milk', 'bread', 'water']
while True:
    user_input = input('Введите команду: ')
    if user_input.lower() == 'stop':
        print('Программа остановлена')
        break
    if len(user_input.split(' ')) == 2:
        command, product = user_input.split(' ')  # text = list
        if command == 'add':
            if product in products:
                print(f'Данный продукт {product} уже есть в списке {products} ')
            else:
                products.append(product)
                print(f'добавили продукт {product} в список {products}')
        elif command == 'del':
            if product in products:
                products.remove(product)
                print(f'Удалили продукт {product} из списка {products}')
            else:
                print(f'Данного продукта {product} нетув списке {products} ')
        else:
            print(f'Вы ввели не верный команду <{command}>')
    else:
        print('Вы ввели не верный текст')
