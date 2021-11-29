# Откройте файл romeo.txt. “Прочитайте” в нем каждую строку. Получите отдельные слова из каждой строки, после чего
# составьте список слов. В списке слова не должны дублироваться. После чего распечатайте список, в котором все слова
# будут отсортированы в алфавитном порядке.
from itertools import groupby

file = open('romeo.txt', mode='r', encoding='utf-8')
data = []
for line in file:
    for i in line:
        data.append(i)
data_str = ''
for i in data:
    if i != '\n':
        data_str = data_str + str(i)
data3 = data_str.split(' ')
print(data_str)
