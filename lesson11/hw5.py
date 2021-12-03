# Создать регулярку Автомобильных номеров Узбекистана
import re


def validateCMD(line):
    # re.search(найди что, найди где)
    r1 = re.search(r'^CMD[0-9]+', line)
    return r1


with open('nomera.txt', mode='r', encoding='utf-8') as file:
    cmd = open('cdm.txt', mode='w', encoding='utf-8')
    data = file.read().split(',')
    for line in data:
        # print(line)
        print(validateCMD(line))

    cmd.close()




