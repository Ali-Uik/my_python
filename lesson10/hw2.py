# Откройте файл romeo.txt. “Прочитайте” в нем каждую строку. Получите отдельные слова из каждой строки, после чего
# составьте список слов. В списке слова не должны дублироваться. После чего распечатайте список, в котором все слова
# будут отсортированы в алфавитном порядке.
from itertools import groupby

file = open('romeo.txt', mode='r', encoding='utf-8')
a = file.read()
b = a.split()
sor = sorted(b)
not_dub = []
for i in sor:
    if i not in not_dub:
        not_dub.append(i)
print(not_dub)
