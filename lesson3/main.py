# Списки - это тип данных, который может содержать в себе много данных
# Создание списков 2 варианта

list1 = []  # пустой список
list2 = list()  # пустой список

contacts = ['Ali', 'Bonu', 'Zara', 'Sabrina', 'Dinara']
# print(contacts)  # печать списка

# как взять определенный элемент списка - индексирование
# print(contacts[1])
# contacts[3] = 'Сабрина'  # учинчи индексдаги (Sabrina)ни узгартирдик
# print(contacts)  # Спатого списка болше нет
# Как узнат размер списка - сколько в нем элементов?
# Усть функция len(длину чего хоти узнать)
# print(len(contacts))
# Как взять последний элемант списка. Это примерно так работает
# print(contacts[len(contacts)-1]) 5-1 -> Dinara
# print(contacts[-1])

# Вставка элементов в список 2 варианта
# 1 вариант - вставка в конкретное место
# insert(куда вставить, и что вставить)
# contacts.insert(3, 'Dilshod')  # учинчи индексга Dilshodни ёзди
# contacts.insert(len(contacts), 'Dilshod')  # охирги индексга Dilshodни ёзди
contacts.append('Sherzod')  # Sherzodни лист охирги индексига ёзди
# print(contacts)

# Удаление 2 способа
# 1 способ удалить и забить метод .remove(Значение)

# contacts.remove('Sherzod')
# print(contacts)

# 2 способ удалить и сохранить метод .pop(Индексу)
# для того чтобы взять номер элемента(индекс) надо использовать метод .index(Значение)
# BonuIndex = contacts.index('Bonu')
# deletedName = contacts.pop(BonuIndex)  # шу ерда Bonu deletedNameда сакланиб колди
# print(f'Удалили {deletedName} из списка {contacts} ')
#
# del contacts[0]  # нолинчи индексдаги Aliни учирди. Агар индекс курсатилмаса listнинг хаммасини учиради
# print(contacts)

# Функция -  это задача, которую можно вызвать в любой момент. Например - len()
# Метод - задача, которая принадлежит объекту. Например - pop()
# Сортируем списки 2 варианта
# 1 вариант
# contacts.sort()  # Постоянная сортировка
# print(contacts)
# contacts.sort(reverse=True)  # тескари тарафга сортировка килади
# print(contacts)
# 2 вариант. Временная сортировка
# print(contacts)
# print(sorted(contacts, reverse=True))
# print(sorted(contacts))
# print(contacts)
# contacts2 = sorted(contacts)  # sortedContacts = sorted(contacts)
# contacts2Reverse = sorted(contacts, reverse=True)
# print(contacts2)
# print(contacts2Reverse)

# Поиск элемента в списка

# if 'Ali' in contacts:
#     print('Hello')
# else:
#     print('Bye')

# Как из строки получить список и наоборот
# Метод .split()
str1 = 'Hello world'
listStrs = str1.split(' ')  # Если в скобках ничего не указать он будет делить по пробелу
print(listStrs)

# names = [1, 'Ali', 2, 'Bonu', 3, 'Dinara', 4, 'Zara', 5, 'Sabrina']
# list_str = []
# list_int = []
# for item in names:
#     if type(item) is int:
#         list_int.append(item)
#     else:
#         list_str.append(item)
# print(list_int)
# print(list_str)