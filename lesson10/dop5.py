# Требуется реализовать функцию longest_words(file), которая выводит слово, имеющее максимальную длину (или список слов,
# если таковых несколько).
def read_last(file):
    file2 = open(file, mode='r', encoding='utf-8')
    data = file2.read()
    data2 = data.split()
    max_str = max(data2, key=len)
    print(max_str)
    file2.close()


read_last('articles.txt')
