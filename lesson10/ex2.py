# Открыть pushkin.txt и скопировать на новую файл
file = open('pushkin.txt', mode='r', encoding='utf-8')
content = file.read()
file2 = open('new2.txt', mode='w', encoding='utf-8')
file2.write(content)
file.close()
file2.close()
