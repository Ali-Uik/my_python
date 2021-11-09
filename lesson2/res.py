zakaz = float(input('Введите сумму заказа: '))
ch = zakaz * 0.18
tax = zakaz * 0.15
sum = zakaz + ch + tax
print(f'Сумма {sum}')
