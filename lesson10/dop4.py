# Напишите функцию read_last(lines, file), которая будет открывать определенный файл file и выводить на печать построчно
# последние строки в количестве lines (на всякий случай проверим, что задано положительное целое число).
# Протестируем функцию на файле «article.txt» со следующим содержимым:

def read_last(file):
    file2 = open(file, mode='r', encoding='utf-8')
    # a = file2.read()
    # b = a.split()
    # print(b)
    for line in file2:
        data = line.split()
        print(data)
    # data2 = data.split()
    # for line in file2:
    #     print(line[0])
    # print(data)


read_last('articles.txt')
