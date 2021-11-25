# Напишите функцию, которая будет принимать количество секунд и возвращать их в днях-часах-минутах-секундах.
# 91000 секунд = 1 день, 1 час, 16 минут, 40 секунд.
a = int(input("Введите число: "))

day_sec = 86400
hour_sec = 3600
min_sec = 60


def sectoDaytoHourtomin(a):
    list1 = []
    if a > day_sec:
        day = a // day_sec
        # print(f'{day} день')
        # list1.append(day)
        b = a % day_sec
        if b > hour_sec:
            hour = b // hour_sec
            # print(f'{hour} час')
            # list1.append(hour)
            c = b % hour_sec
            if c > min_sec or b > min_sec:
                hour = 0
                if c:
                    minut = c // min_sec
                elif b:
                    minut = b // min_sec
                # print(f'{minut} минути')
                # list1.append(minut)
                    d = c % min_sec
                # print(f'{d} секунд')
                # list1.append(d)
            else:
                minut = 0
                # d = c
    print(f'{day} день, {hour} час, {minut} минут, {d} секунд')


sectoDaytoHourtomin(a)
