# Откройте файл mbox-short.txt, “прочитайте” каждую строку в этом файле и найдите строки, соответствующие данной:
# “From Stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008”
# Затем распечатайте все ВХОДЯЩИЕ email адреса и из общее количество.
# Для решения данной задачи используйте методы строк.

file = open('mbox-short.txt', mode='r', encoding='utf-8')

for line in file:
    if line.startswith('From '):
        data = line.split(' ')[1]
        print(data)
file.close()





