# Задача «Лесенка» По данному натуральному n ≤ 9 выведите лесенку из n ступенек, i-я ступенька состоит из чисел
# от 1 до i без пробелов.
n = int(input('Введите цело число: '))

if 1 <= n <= 9:
    for i in range(n):
        for item in range(i):
            if item >= 1:
                print(item)
