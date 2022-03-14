list1 = [i for i in range(11)]
list2 = []
print(list1)
for k in list1:
    if k > 0:
        n = 1
        print(f'k={k}')
        while n <= k:
            print(f'n = {n}, k = {k}')
            tub = k % n
            print(f'tub = {tub}')
            if tub == 0:
                print(f'k qushildi {k}')
                list2.append(k)
            n = n + 1
list3 = list2.pop(0)
list4 = set(list3)
print(list2)
print(set(list4))
