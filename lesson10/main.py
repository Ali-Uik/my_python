# ASCII
# Open

# file = open('byron.txt')  # открываем файл
# content = file.read()  # читаем
# print(content)
# file.close()  # закрываем файл

# UTF8
# 'r' - прочитать информацию
# 'w' - записать информацию, если файла не сущ. то создаст
# 'а' - дописать информацию, если файла не сущ. то будеть орать ОШИБКА
# 'rb' - прочитат байты файла
# 'wb' - записать байти файла
# file = open('pushkin.txt', mode='r', encoding='utf-8')
# content = file.read()
# print(content)
# print(file.encoding)  # выведет кодировку файла
# print(file.writable())  # скажет можно ли в файл записывать
# print(file.readable())  # скажет можно ли файл читать
# file.close()

# file = open('text.txt', mode='w', encoding='utf-8')
# content = 'Hello world\n'   # \n - Переход на новоу строку
# file.write(content)
# file.close()
file = open('text.txt', mode='a', encoding='utf-8')  # добовляеть строку
content = 'Hello world\n'  # \n - Переход на новоу строку
file.write(content)
file.close()



