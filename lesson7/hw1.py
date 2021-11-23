a = input('Введите:')


def palindrom(a):
    if a == a[::-1]:
        return "yes"
    else:
        return "no"


d = palindrom(a)
print(d)
