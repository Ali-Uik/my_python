# Исключения и оброботка ошибок
# print(name)
# try:
#     # print(name)
#     list1 = [1, 2, 3]
#     print(list1[5])
# # except Exception as e:  # Что надо делать если произошло ошибка
# except (NameError, IndexError) as e:  # Что надо делать если произошло ошибка
#     e.__str__ = "ошибка, такой переменной нет"
#     print('Произошло ошибка', e)
#     print('Произошло ошибка', e.__class__)
#     print('Произошло ошибка', e.__class__.__name__)
#     print('Произошло ошибка', e.__str__)


# Бесконечно спрашиваем у пользователя номер
# Если введеннный текст не оказался числом - продолжить работу но вывести текст ошибки
# Если число == 1 - распечатать name которого не существует-вывести текст ошибки
# Если число == 2 - вывести 6 элемент из списка (из 3х элементов)-вывести имя ошибки
# Если число == 3 - попробовать разделить 10/0 - вывести свой текст ошибки
#  мой вариант
# while True:
#     data = int(input('Введите целое число: '))
#     # print(data)
#     if data == 1:
#         try:
#             print(name)
#         except Exception as e:
#             print('ошибка:', e)
#     elif data == 2:
#         list1 = [1, 2, 3]
#         try:
#             print(list1[6])
#         except Exception as e:
#             print('ошибка:', e)
#     elif data == 3:
#         try:
#             print(10 / 0)
#         except Exception as e:
#             print('10 ni 0 ga bulib bulmaydi', e)
#     else:
#         print(data)

# ---------------------------------------------------------------------------------------------------------------------

# Вариант от учителя

# while True:
#     number = input('Введите число: ')
#     try:
#         num = int(number)
#         if num == 1:
#             try:
#                 print(name)
#             except NameError:
#                 print(NameError)
#         elif num == 2:
#             try:
#                 list1 = [1, 2, 3]
#                 print(list1[6])
#             except IndexError:
#                 print(IndexError.__name__)
#         elif num == 3:
#             try:
#                 print(10 / 0)
#             except ZeroDivisionError:
#                 ZeroDivisionError.__str__ = f'На 0 делить нельзя'
#                 print(ZeroDivisionError.__str__)
#     except Exception as e:
#         print('Надо было писать число', e)


# Регелярные выражения
# Текст - который проверяет другой текст
# import string
#
#
# def validate_name(name):
#     for letter in name:
#         if letter in string.punctuation or letter in string.digits:
#             return False
#     return True
#
#
# def validate_email(email):
#     if '@' in email and '.' in email:
#         return True
#     return False
#
#
# def validate_age(age):
#     try:
#         if 10 <= int(age) <= 99:
#             return True
#         else:
#             return False
#     except:
#         return False
#
#
# with open('registrations.txt', mode='r', encoding='utf-8') as file:
#     good = open('good.txt', mode='w', encoding='utf-8')
#     bad = open('bad.txt', mode='w', encoding='utf-8')
#     for line in file:
#         if len(line.split(' ')) != 3:
#             bad.write(line)
#         else:
#             # 1. Имя - текстом
#             # 2. Почта - @ .
#             # 3. Возрасть - 10 - 99
#             data = line.split(' ')
#             data_for_name = validate_name(data[0])
#             data_for_email = validate_email(data[1])
#             data_for_age = validate_age(data[2])
#             if data_for_name and data_for_email and data_for_age:
#                 good.write(line)
#             else:
#                 bad.write(line)
#
#     good.close()
#     bad.close()

import re

#
#
# def validate(line):
#     # re.search(найди что, найди где)
#     r1 = re.search(r'^[а-яА-ЯёЁ]+ [a-zA-Z0-9_.]+@[a-z]+.[a-z]+ [0-9]{2}$', line)
#     return r1
#
#
# with open('registrations.txt', mode='r', encoding='utf-8') as file:
#     good = open('good.txt', mode='w', encoding='utf-8')
#     bad = open('bad.txt', mode='w', encoding='utf-8')
#     for line in file:
#         if validate(line):
#             good.write(line)
#         else:
#             bad.write(line)
#     good.close()
#     bad.close()

print(re.split(r'\W+', 'Привет меня зовут Евгений'))
str1 = 'Этот урок прошол 01.12.2021. Следующий урок 04.12.2021'
print(re.findall(r'\d\d.\d\d.\d{4}', str1))
