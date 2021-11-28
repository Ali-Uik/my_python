# While True
# input
# записывать все что пишет пользователь
# если написал STOP остановаить и закрыть файл


while True:
    content = input('Введите текст:')
    file = open('new.txt', mode='a', encoding='utf-8')
    file.write(content+'\n')
    if content == 'stop':
        file.close()
        break
