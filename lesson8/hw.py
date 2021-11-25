# Напишите функцию, которая будет принимать количество секунд и возвращать их в днях-часах-минутах-секундах.
# 91000 секунд = 1 день, 1 час, 16 минут, 40 секунд.
a = int(input("Введите число: "))

day_sec = 86400
hour_sec = 3600
min_sec = 60


def sectoDaytoHourtomin(a):
    if a >= day_sec:
        day = a // day_sec
        rem_day = a % day_sec
        # print(day)
        if rem_day >= 3600:
            hour = rem_day // hour_sec
            rem_hour = rem_day % hour_sec
            # print(hour)
            if rem_hour >= min_sec:
                minutes = rem_hour // min_sec
                seconds = rem_hour % min_sec
                # print(minutes,seconds)
                print(f'{day} день, {hour} час, {minutes} минут, {seconds} секунд')

    else:
        if a >= 3600:
            hour = a // hour_sec
            rem_hour = a % hour_sec
            # print(hour)
            if rem_hour >= min_sec:
                minutes = rem_hour // min_sec
                seconds = rem_hour % min_sec
                # print(minutes,seconds)
                print(f'0 день, {hour} час, {minutes} минут, {seconds} секунд')


sectoDaytoHourtomin(a)
