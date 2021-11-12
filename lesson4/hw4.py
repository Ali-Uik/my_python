num = int(input('Введите число: '))
list1 = [i for i in range(num + 1)]
even = []
odd = []
for i in list1:
    if i % 2 == 0:
        even.append(i)
    elif i % 2 == 1:
        odd.append(i)

print(even)
print(sum(even))
print(odd)
print(sum(odd))