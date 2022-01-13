# A = int(input('A dan N gacha tub sonlarni topamiz A='))
# N = int(input('N='))
# for k in range(A, N + 1):
#     prime = True
#     for i in range(2, k):
#         if k % i == 0:
#             prime = False
#             break
#     if prime:
#         print('{} - tub sonlar'.format(k))
#
print('ABC uchburchak perimetri p ni va yuzi S ni topamiz.')
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if a + b > c and a + c > b and b + c > a:
    print(f'ABC uchburchakning perimetri p={a + b + c}')
    print(
        f'ABC uchburchakning yuzi S = {((a + b + c) / 2 * (a + b - c) / 2 * (a + c - b) / 2 * (b + c - a) / 2) ** (1 / 2)}')
    if (a ** 2 + b ** 2 > c ** 2) or (a ** 2 + c ** 2 > b ** 2) or (b ** 2 + c ** 2 > a ** 2):
        print('ABC uchburchak o\'tkir burchakli uchburchak')
    elif (a ** 2 + b ** 2 == c ** 2) or (a ** 2 + c ** 2 == b ** 2) or (b ** 2 + c ** 2 == a ** 2):
        print('ABC uchburchak to\'g\'ri burchakli uchburchak')
    else:
        print('ABC uchburchak o\'tmas burchakli uchburchak')
else:
    print('bunday uchburchak mavjud emas')
