# Есть словарь кодов товаров и словарь количества товара на складе.
goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}
store = {
    '12345': [
        {
            'quantity': 27,
            'price': 42
        },
    ],
    '23456': [
        {
            'quantity': 22,
            'price': 510
        },
        {
            'quantity': 32,
            'price': 520
        },
    ],
    '34567': [
        {
            'quantity': 2,
            'price': 1200
        },
        {
            'quantity': 1,
            'price': 1150
        },
    ],
    '45678': [
        {
            'quantity': 50,
            'price': 100
        },
        {
            'quantity': 12,
            'price': 95
        },
        {
            'quantity': 43,
            'price': 97
        },
    ],
}

# for keyGoods, valueGoods in goods.items():
#     for keyStore, valueStore in store.items():
#         for i in valueStore:
#             for key, value in i.items():
#                 # print(type(i))
#                 # print(key)
#                 # print(value)
#                 if valueGoods == keyStore:
#                     print(
#                         f'Порядковый номер товара: {valueGoods}\nНаименовиние товара: {keyGoods}\nОбщее количество: '
#                         f' ')

for product_name, product_id in goods.items():
    # print(product_name, product_id)
    total_quantity = 0
    total_sum = 0
    for data in store[product_id]:
        price = data['quantity']*data['price']
        total_quantity += data['quantity']
        total_sum = total_sum + price
        # print(total_quantity)
    print(f'Номер продукта: {product_id}')
    print(f'Название продукта: {product_name}')
    print(f'Общая количество продукта: {total_quantity}')
    print(f'Общая стоимост: {total_sum}')
