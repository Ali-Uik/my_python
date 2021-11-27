import time
a = int(input("Введите число: "))
start = time.time()
list1 = [i for i in range(a)]
finish = time.time()

print(finish-start)
print(list1)
