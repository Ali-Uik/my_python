import requests
import psycopg2
from pprint import pprint

db = psycopg2.connect(
    database='lesson19',
    host='localhost',
    user='postgres',
    password='123'
)
cursor = db.cursor()
cursor.execute(
    '''
    SELECT product_name, unit_price,
CASE
	WHEN unit_price >= 80 THEN 'очен дорого'
	WHEN unit_price >= 20 AND unit_price < 80 THEN 'нормально'
	WHEN unit_price >= 1 AND unit_price < 20 THEN 'дешево'
	ELSE 'цена не указана'
END AS price_description
FROM products ORDER BY unit_price;
    '''
)

products = cursor.fetchall()  # Для получения ответов с более чем 1 данных
pprint(products)

cursor.execute(
    '''
    SELECT AVG(unit_price) FROM products;

    '''
)
# avg = cursor.fetchone()
avg1 = cursor.fetchone()[0]
# print(avg)
print(avg1)

# Создат две таблицы для users и posts

cursor.execute(
    '''
    DROP TABLE IF EXISTS users;
    CREATE TABLE IF NOT EXISTS users
        id
    '''
)


