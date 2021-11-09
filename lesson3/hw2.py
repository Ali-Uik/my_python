f_name = input('Имя: ')
l_name = input('Фамилия: ')
age = input('Возраст:')
data = []
if f_name:
    data.append(f_name)
else:
    print('Empty')
if l_name:
    data.append(l_name)
else:
    print('Empty')
if age:
    data.append(age)
else:
    print('Empty')
print(data)


