A = int(input('A dan N gacha tub sonlarni topamiz A='))
N = int(input('N='))
for k in range(A, N + 1):
    prime = True
    for i in range(2, k):
        if k % i == 0:
            prime = False
            break
    if prime:
        print('{} - tub sonlar'.format(k))
