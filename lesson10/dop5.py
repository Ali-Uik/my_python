# Требуется реализовать функцию longest_words(file), которая выводит слово, имеющее максимальную длину (или список слов,
# если таковых несколько).
# def read_last(file):
#     file2 = open(file, mode='r', encoding='utf-8')
#     data = file2.read()
#     data2 = data.split()
#     max_str = max(data2, key=len)
#     print(max_str)
#     file2.close()
#
#
# read_last('articles.txt')

# Nodir's version
file = open('article.txt', mode='r', encoding='utf-8')
a = file.read()
b = a.split()
print(b)


def longest(words):
    c = ''
    for i in b:
        if len(i) > len(c):
            c = i
    print('longest one is ', c)


longest(b)
file.close()
