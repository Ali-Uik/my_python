age = int(input('Введите свой возраст: '))

if age <= 18:
    print('Вам нужно учиться')
elif 18 < age < 50:
    print('Вам нужно работать')
elif 50 < age <= 59:
    print('Вам скоро на пенсию')
elif 50 < age < 100:
    print('Вы пенсионер')
else:
    print('Вы дебил чтоли')
