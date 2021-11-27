import time

a = int(input("Введите число: "))
start = time.time()
list1 = [i for i in range(1, a)]
finish = time.time()

print(finish - start)

