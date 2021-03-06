import math

# Упражнение 1. Почтовый адрес
# Напишите несколько строк кода, выводящих на экран ваше имя и почтовый адрес. Адрес напишите в формате,
# принятом в вашей стране. Никакого ввода от пользователя ваша первая программа принимать не будет,
# только вывод на экран и больше ничего.
# name = 'Baltaev Izzatbek'
# address = 'Toshkent shahri, M.Ulug\'bek tumani, Buyuk ipak yo\'li ko\'chasi 133-uy 48-honadon'
# print(f'Mening to\'liq ismim: {name}. Yashash manzilim: {address}')

# ______________________________________________________________________________________________________________________

# Упражнение 2. Приветствие
# Напишите программу, запрашивающую у пользователя его имя. В ответ
# на ввод на экране должно появиться приветствие с обращением по имени,
# введенному с клавиатуры ранее.
# name = input('Введите свое имя:')
# print(f'Hello, {name}')


# ______________________________________________________________________________________________________________________


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


# ______________________________________________________________________________________________________________________


# Упражнение 4. Площадь садового участка
# Создайте программу, запрашивающую у пользователя длину и ширину
# садового участка в футах. Выведите на экран площадь участка в акрах.
# l = float(input('Введите длину участка: '))
# w = float(input('Введите ширину участка: '))
# s = l * w
# arc = s/43560
# print(f'Площадь участка в арках {arc}\nШлощадь участка в футах {s}')

# ______________________________________________________________________________________________________________________

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

# ______________________________________________________________________________________________________________________

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


# ______________________________________________________________________________________________________________________


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


# ______________________________________________________________________________________________________________________


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


# ______________________________________________________________________________________________________________________

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


# a = int(input('Первое целое цисло: '))
# b = int(input('Второе целое цисло: '))
# plus = a + b
# minus = a - b
# mult = a * b
# c = a // b
# d = a % b
# f = math.log10(a)
# e = a ** b
# print(
#     f'Сумма a и b: {plus}\nРазница между a и b: {minus}\nПроизведение a и b: {mult}\nЧастное от деления a на b: {c}'
#     f'\nОстаток от деления a на b:{d}\nДесятичный логарифм числа a:{f}\nРезультат возведения числа a в степень b:{e}')


# ______________________________________________________________________________________________________________________

# Упражнение 11. Потребление топлива
# (13 строк)
# В США потребление автомобильного топлива исчисляется в милях на галлон (miles-per-gallon – MPG). В то же время в
# Канаде этот показатель обычно выражается в литрах на 100 км (liters-per-hundred kilometers – L/100 km). Используйте
# свои исследовательские способности, чтобы определить формулу перевода первых единиц исчисления в последние. После
# этого напишите программу, запрашивающую у пользователя показатель потребления топлива автомобилем в американских
# единицах и выводящую его на экран в канадских единицах.

# litr = input("Введите литри:")
# gallon = input("Введите галлоны:")
# if litr:
#     print(f'{litr} литров ровно {float(litr) * 0.26} галлонов')
# if gallon:
#     print(f'{gallon} галлонов ровно {float(gallon) * 3.785412} литров')


# ______________________________________________________________________________________________________________________

# Упражнение 12. Расстояние между точками на Земле
# (27 строк)
# Как известно, поверхность планеты Земля искривлена, и расстояние между точками, характеризующимися одинаковыми
# градусами по долготе,может быть разным в зависимости от широты. Таким образом, для вычисления расстояния между двумя
# точками на Земле одной лишь теоремой Пифагора не обойтись.Допустим, (t1, g1) и (t2, g2) – координаты широты и долготы
# двух точек на поверхности Земли. Тогда расстояние в километрах между ними с учетом
# искривленности планеты можно найти по следующей формуле:
# distance = 6371,01´arccos(sin(t1)´sin(t2) + cos(t1)´cos(t2)´cos(g1 - g2)).
# Примечание. Число 6371,01 в этой формуле, конечно, было выбрано не случайнои представляет собой среднее значение
# радиуса Земли в километрах.Напишите программу, в которой пользователь будет вводить координаты двух точек на Земле
# (широту и долготу) в градусах. На выходе мы должны получить расстояние между этими точками при следовании по
# кратчайшему пути по поверхности планеты. Подсказка. Тригонометрические функции в Python оперируют радианами. Таким
# образом, вам придется введенные пользователем величины из градусов перевестив радианы, прежде чем вычислять расстояние
# между точками. В модуле math есть удобная функция с названием radians-Функции:radians, служащая как раз для перевода
# градусов в рад

# first_point_latitude = float(input('Первая точка широта:'))
# first_point_longitude = float(input('Первая точка долгота:'))
# second_point_latitude = float(input('Вторая точка широта:'))
# second_point_longitude = float(input('Вторая точка долгота:'))
# first_point_latitude_radian = math.radians(first_point_latitude)
# first_point_longitude_radian = math.radians(first_point_longitude)
# second_point_latitude_radian = math.radians(second_point_latitude)
# second_point_longitude_radian = math.radians(second_point_longitude)
# distance = 6371.01 * math.acos(math.sin(first_point_latitude_radian) * math.sin(second_point_latitude_radian) +
#                                math.cos(first_point_latitude_radian) * math.cos(second_point_latitude_radian) *
#                                math.cos(first_point_longitude_radian - second_point_longitude_radian))
# print(distance.__round__(2))

# ______________________________________________________________________________________________________________________


# Упражнение 13. Размен
# (Решено. 35 строк)
# Представьте, что вы пишете программное обеспечение для автоматической кассы в магазине самообслуживания. Одной из
# функций, заложенных в кассу, должен быть расчет сдачи в случае оплаты покупателем наличными.
# Напишите программу, которая будет запрашивать у пользователя сумму сдачи в центах. После этого она должна рассчитать и
# вывести на экран, сколько и каких монет потребуется для выдачи указанной суммы, при условии что должно быть
# задействовано минимально возможное количество монет. Допустим, у нас есть в распоряжении монеты достоинством в
# 1, 5, 10, 25 центов, а также в 1 (loonie) и 2 (toonie) канадских доллара.
# Примечание. Монета номиналом в 1 доллар была выпущена в Канаде в 1987 году.
# Свое просторечное название (loonie) она получила от изображения полярной гагары
# (loon) на ней. Двухдолларовая монета, вышедшая девятью годами позже, была прозвана toonie, как комбинация из слов два
# (two) и loonie.
# hundred_thousand = 100000
# fifty_thousand = 50000
# twenty_thousand = 20000
# ten_thousand = 10000
# five_thousand = 5000
# two_thousand = 2000
# thousand = 1000
# five_hundred = 500
# two_hundred = 200
# hundred = 100
# fifty = 50
# bill = ['50 000 so\'mlik: ', '20 000 so\'mlik: ', '10 000 so\'mlik: ', '5 000 so\'mlik: ', '2 000 so\'mlik: ',
#         '1 000 so\'mlik: ', '500 so\'mlik: ', '200 so\'mlik: ', '100 so\'mlik: ', '50 so\'mlik: ']
# changeList = []
# price = float(input('Umumiy summani kiriting: '))
# cash = float(input('Mijoz to\'lov qilgan summasini kiriting: '))
#
# if price >= 100000:
#     price = price - price * 0.01
#     change = cash - price
#     print(f'1% skidkadan keyingi summe: {price}\nQaytim: {change}')
#     change_fifty_thousand = change // fifty_thousand
#     changeList.append(change_fifty_thousand)
#     change_twenty_thousand = change % fifty_thousand // twenty_thousand
#     changeList.append(change_twenty_thousand)
#     change_ten_thousand = change % fifty_thousand % twenty_thousand // ten_thousand
#     changeList.append(change_ten_thousand)
#     change_five_thousand = change % fifty_thousand % twenty_thousand % ten_thousand // five_thousand
#     changeList.append(change_five_thousand)
#     change_two_thousand = change % fifty_thousand % twenty_thousand % ten_thousand % five_thousand // two_thousand
#     changeList.append(change_two_thousand)
#     change_thousand = change % fifty_thousand % twenty_thousand % ten_thousand % five_thousand % two_thousand // thousand
#     changeList.append(change_thousand)
#     change_five_hundred = change % fifty_thousand % twenty_thousand % ten_thousand % five_thousand % two_thousand % thousand // five_hundred
#     changeList.append(change_five_hundred)
#     change_two_hundred = change % fifty_thousand % twenty_thousand % ten_thousand % five_thousand % two_thousand % thousand % five_hundred // two_hundred
#     changeList.append(change_two_hundred)
#     change_hundred = change % fifty_thousand % twenty_thousand % ten_thousand % five_thousand % two_thousand % thousand % five_hundred % two_hundred // hundred
#     changeList.append(change_hundred)
#     change_fifty = change % fifty_thousand % twenty_thousand % ten_thousand % five_thousand % two_thousand % thousand % five_hundred % two_hundred % hundred // fifty
#     changeList.append(change_fifty)
#     print(changeList)
#
#
# else:
#     change = cash - price
#     change_fifty_thousand = change // fifty_thousand
#     changeList.append(change_fifty_thousand)
#     change_twenty_thousand = change % fifty_thousand // twenty_thousand
#     changeList.append(change_twenty_thousand)
#     change_ten_thousand = change % fifty_thousand % twenty_thousand // ten_thousand
#     changeList.append(change_ten_thousand)
#     change_five_thousand = change % fifty_thousand % twenty_thousand % ten_thousand // five_thousand
#     changeList.append(change_five_thousand)
#     change_two_thousand = change % fifty_thousand % twenty_thousand % ten_thousand % five_thousand // two_thousand
#     changeList.append(change_two_thousand)
#     change_thousand = change % fifty_thousand % twenty_thousand % ten_thousand % five_thousand % two_thousand // thousand
#     changeList.append(change_thousand)
#     change_five_hundred = change % fifty_thousand % twenty_thousand % ten_thousand % five_thousand % two_thousand % thousand // five_hundred
#     changeList.append(change_five_hundred)
#     change_two_hundred = change % fifty_thousand % twenty_thousand % ten_thousand % five_thousand % two_thousand % thousand % five_hundred // two_hundred
#     changeList.append(change_two_hundred)
#     change_hundred = change % fifty_thousand % twenty_thousand % ten_thousand % five_thousand % two_thousand % thousand % five_hundred % two_hundred // hundred
#     changeList.append(change_hundred)
#     change_fifty = change % fifty_thousand % twenty_thousand % ten_thousand % five_thousand % two_thousand % thousand % five_hundred % two_hundred % hundred // fifty
#     changeList.append(change_fifty)
#     print(changeList)
#
# length = len(changeList)
# for item in range(length):
#     changeDict = {
#         bill[item]: changeList[item]
#     }
#     print(changeDict)


# ______________________________________________________________________________________________________________________

# Упражнение 14. Рост
# (Решено. 16 строк) Многие люди на планете привыкли рассчитывать рост человека в футах и дюймах, даже если в их стране
# принята метрическая система. Напишите программу, которая будет запрашивать у пользователя количество футов, а затем
# дюймов в его росте. После этого она должна пересчитать рост в сантиметры и вывести его на экран.
# user = int(input('Введите рост в дюймах:'))
#
#
# class User:
#     def __init__(self, height):
#         self.height = height
#
#     def inch(self):
#         return self.height
#
#     def inch_to_sm(self):
#         return self.height * 2.54
#
#     def inch_to_fut(self):
#         return self.height * 0.0833333
#
#
# print(f'Ваш рост в дюймах: {User(user).inch()}')
# print(f'Ваш рост в сантиметрах: {User(user).inch_to_sm()}')
# print(f'Ваш рост в футах: {User(user).inch_to_fut()}')

# ______________________________________________________________________________________________________________________
