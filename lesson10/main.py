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
# file = open('text.txt', mode='a', encoding='utf-8')  # добовляеть строку
# content = 'Hello world\n'  # \n - Переход на новоу строку
# file.write(content)
# file.close()

# Конструкция которая автоматически закрывает файл with open

# with open('pushkin.txt', mode='r', encoding='utf-8') as file:
#     new_file = open('new_file.txt', mode='w', encoding='utf-8')
#     content = file.read()
#     print('Закрыт ли файл?', file.closed)
#     new_file.write(content)
#     new_file.close()
# print('Закрыт ли файл?', file.closed)

# Работа с данными в не текстовых файлах
# import os
# if 'picture' not in os.listdir():  # Создаем папку
#     os.mkdir('picture')
# file = open('nature.jpg', mode='rb')
# picture = file.read()
# for i in range(1, 11):
#     new_picture = open(f'picture/nature_copy{i}.jpg', mode='wb')
#     new_picture.write(picture)
#     new_picture.close()
# file.close()
# for i in range(1,11):
#     os.remove(f'picture/nature_copy{i}.jpg')
# os.rmdir('picture')
str1 = 'Hello'
str1_8 = str1.encode(encoding='utf-8')
str1_16 = str1.encode(encoding='utf-16')
str1_32 = str1.encode(encoding='utf-32')
str1_cp866 = str1.encode(encoding='cp866')
str1_cp1251 = str1.encode(encoding='cp1251')
print(str1_8)
print(str1_16)
print(str1_32)
print(str1_cp866)
print(str1_cp1251)
