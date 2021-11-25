# Создайте функцию , которая принимает целое число и возвращает сумму цифр целого числа

a = input("Введите число: ")
b = []
for i in a:
    if i:
        b.append(int(i))
    else:
        print('Error')

# n = [a]
print(sum(b))
