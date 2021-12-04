# Создать регулярку Автомобильных номеров Узбекистана
import re


def validateCMD(line):
    # re.search(найди что, найди где)
    r1 = re.search(r'CMD[0-9]+', line)
    # return r1
    return r1


def validateUN(line):
    # re.search(найди что, найди где)
    r1 = re.search(r'UN[0-9]+', line)
    # return r1
    return r1


def validatePAA(line):
    # re.search(найди что, найди где)
    r1 = re.search(r'PAA[0-9]+', line)
    # return r1
    return r1

def validateTASH(line):
    # re.search(найди что, найди где)
    r1 = re.search(r'01[0-9]+[A-Z]+', line)
    # return r1
    return r1


with open('nomera.txt', mode='r', encoding='utf-8') as file:
    cmd = open('cmd.txt', mode='w', encoding='utf-8')
    un = open('un.txt', mode='w', encoding='utf-8')
    paa = open('paa.txt', mode='w', encoding='utf-8')
    tash = open('tash.txt', mode='w', encoding='utf-8')
    data = file.read().split(',')
    for line in data:
        # print(line)
        if validateCMD(line):
            cmd.write(line)
        elif validateUN(line):
            un.write(line)
        elif validatePAA(line):
            paa.write(line)
        elif validateTASH(line):
            # tash.write(line)
            print(line)

    cmd.close()
    un.close()
    paa.close()
    tash.close()
