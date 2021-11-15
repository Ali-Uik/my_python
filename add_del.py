products = ['milk', 'bread', 'doll']
while True:
    prod = input('введите имя товара: ')
    prod_split = prod.split('-')
    if prod_split[0] == 'stop':
        print(products)
        break
    elif prod_split[0] == 'add':
        if prod_split[1] in products:
            print(f'{prod_split[1]} в списке {products} уже существует. Вы не можете добавить! ')
        else:
            products.append(prod_split[1])
            print(f'В список добавлено продукт {prod_split[1]}. {products}')
    elif prod_split[0] == 'del':
        if prod_split[1] in products:
            products.remove(prod_split[1])
            print(f'Из списка удалено продукт {prod_split[1]}. {products}')
        else:
            print(f'{prod_split[1]} в списке {products} не существует. Так что вы не можете удалить этот продукт!!!! ')
    else:
        print('Вы ввели не корректную команду или ничего не ввели')
