# Упражнение 1. Почтовый адрес
# Напишите несколько строк кода, выводящих на экран ваше имя и почтовый адрес. Адрес напишите в формате,
# принятом в вашей стране. Никакого ввода от пользователя ваша первая программа принимать не будет,
# только вывод на экран и больше ничего.
# name = 'Baltaev Izzatbek'
# address = 'Toshkent shahri, M.Ulug\'bek tumani, Buyuk ipak yo\'li ko\'chasi 133-uy 48-honadon'
# print(f'Mening to\'liq ismim: {name}. Yashash manzilim: {address}')

# Упражнение 2. Приветствие
# Напишите программу, запрашивающую у пользователя его имя. В ответ
# на ввод на экране должно появиться приветствие с обращением по имени,
# введенному с клавиатуры ранее.
# name = input('Введите свое имя:')
# print(f'Hello, {name}')

# Упражнение 3. Площадь комнаты
# Напишите программу, запрашивающую у пользователя длину и ширину
# комнаты. После ввода значений должен быть произведен расчет площади
# комнаты и выведен на экран. Длина и ширина комнаты должны вводиться
# в формате числа с плавающей запятой. Дополните ввод и вывод единицами
# измерения, принятыми в вашей стране. Это могут быть футы или метры.
# l = float(input('Введите длину комнаты: '))
# w = float(input('Введите ширину комнаты: '))
# s = l * w
# print(f'Площадь команаты {s} кв.м')

# Упражнение 4. Площадь садового участка
# Создайте программу, запрашивающую у пользователя длину и ширину
# садового участка в футах. Выведите на экран площадь участка в акрах.
# l = float(input('Введите длину участка: '))
# w = float(input('Введите ширину участка: '))
# s = l * w
# arc = s/43560
# print(f'Площадь участка в арках {arc}\nШлощадь участка в футах {s}')

# Упражнение 5. Сдаем бутылки
# Во многих странах в стоимость стеклотары закладывается определенный
# депозит, чтобы стимулировать покупателей напитков сдавать пустые бутылки. Допустим, бутылки объемом 1 литр и меньше
# стоят # $0,10, а бутылки большего объема – $0,25.Напишите программу, запрашивающую у пользователя количество бутылок
# каждого размера. На экране должна отобразиться сумма, которую можно выручить, если сдать всю имеющуюся посуду.
# Отформатируйте вывод так, чтобы сумма включала два знака после запятой и дополнялась слева символом доллара.
# l = int(input('Введите количество бутилок объемом 1 литр и меньше: '))
# w = int(input('Введите количество бутилок объемом больше 1 литра:'))
# sum1 = l * 0.10
# sum2 = w * 0.25
# sum = sum1 + sum2
# print(f'Total: {sum} $')

# Упражнение 6. Налоги и чаевые
# Программа, которую вы напишете, должна начинаться с запроса у пользователя суммы заказа в ресторане. После этого
# должен быть произведен расчет налога и чаевых официанту. Вы можете использовать принятую в вашем регионе налоговую
# ставку для подсчета суммы сборов. В качестве чаевых мы оставим 18 % от стоимости заказа без учета налога. На выходе
# программа должна отобразить отдельно налог, сумму чаевых и итог, включая обе составляющие. Форматируйте вывод таким
# образом, чтобы все числа отображались с двумя знаками после запятой.
# a = float(input('Введите сумму заказа:'))
# tips = a * 0.18
# tax = a * 0.15
# print(f'Сумма заказа: {a} \nЧаевые: {tips} \nНалоги: {tax} \nОбщая сумма: {a + tips + tax}')

# Упражнение 7. Сумма первых n положительных чисел
# (Решено. 11 строк)
# Напишите программу, запрашивающую у пользователя число и подсчитывающую сумму натуральных положительных чисел от 1 до
# введенного пользователем значения. Сумма первых n положительных чисел может быть рассчитана по формуле:
# n = int(input('Введите целое число: '))
# sum = n*(n+1)/2
# print(sum)
# Упражнение 8. Сувениры и безделушки
# (15 строк)
# Интернет-магазин занимается продажей различных сувениров и безделушек. Каждый сувенир весит 75 г,
# а безделушка – 112 г. Напишите программу, запрашивающую у пользователя количество тех и других покупок,после чего
# выведите на экран общий вес посылки.
# s = int(input('Введите количество сувениров: '))
# b = int(input('Введите количество безделушек: '))
# s_m = 75
# b_m = 112
# sum = s_m * s + b_m * b
# if sum >= 1000:
#     sum_kg = sum / 1000
#     print(f'Общый вес:{sum_kg} килограмм')
# else:
#     print(f'Общый вес:{sum} грамм')

# Упражнение 9. Сложные проценты
# (19 строк)
# Представьте, что вы открыли в банке сберегательный счет под 4 % годовых. Проценты банк рассчитывает в конце года и
# добавляет к сумме счета. Напишите программу, которая запрашивает у пользователя сумму первоначального депозита,
# после чего рассчитывает и выводит на экран сумму на счету в конце первого, второго и третьего годов. Все суммы должны
# быть округлены до двух знаков после запятой.

# a = float(input('Введите первоначальный взнос: '))
# b = []
# for i in range(3):
#     a = a + a * 0.04
#     b.append(a)
# print(
#     f'Первоначальный взнос:{a}\nПервый год:{b[0].__round__(2)}\nВторой год:{b[1].__round__(2)}'
#     f'\nТретий год:{b[2].__round__(2)}')

# Упражнение 10. Арифметика
# (Решено. 22 строки)
# Создайте программу, которая запрашивает у пользователя два целых числа a и b, после чего выводит на экран результаты
# следующих математических операций:
# сумма a и b;
# разница между a и b;
# произведение a и b;
# частное от деления a на b;
# остаток от деления a на b;
# десятичный логарифм числа a;
# результат возведения числа a в степень b.
import math
a = int(input('Первое целое цисло: '))
b = int(input('Второе целое цисло: '))
plus = a + b
minus = a - b
mult = a * b
c = a // b
d = a % b
