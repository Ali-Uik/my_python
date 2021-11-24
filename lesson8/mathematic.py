# Написать функции решения квадрата числа
# куба числа
# квадратного уровнения
# вычесление корня
# Вывод всех простых чисел от 0 до поданного n

def kv(x):
    return x * x


def kub(x):
    return x * x * x


def urav(a, b, c):
    d = b ** 2 - 4 * a * c
    if d < 0:
        return False
    elif d == 0:
        return -b / 2 * a
    else:
        return [(-b - d ** 0.5) / 2 * a, (-b + d ** 0.5) / 2 * a]


def koren(x):
    return x ** 0.5


def primeNumbers(n):
    count = 0
    pn = []
    for i in range(2, n + 1):
        for j in range(2, i):
            if i % j == 0:
                count = count + 1
        if count == 0:
            pn.append(i)
        else:
            count = 0
    return pn
