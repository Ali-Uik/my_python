import requests
import psycopg2
from pprint import pprint

# Маълумотлар базасига уланиш
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
# products = cursor.fetchone()  # Для получения 1 данных
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
    DROP TABLE IF EXISTS posts;
    DROP TABLE IF EXISTS users;
    CREATE TABLE IF NOT EXISTS users(
        user_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
        name VARCHAR(100),
        username VARCHAR(100),
        email TEXT
        );
    CREATE TABLE IF NOT EXISTS posts(
        post_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
        user_id INTEGER REFERENCES users(user_id),
        title TEXT,
        body TEXT
        );
    '''
)

users = requests.get('https://jsonplaceholder.typicode.com/users').json()
posts = requests.get('https://jsonplaceholder.typicode.com/posts').json()
for user in users:
    name = user['name']
    username = user['username']
    email = user['email']
    cursor.execute(
        '''
        INSERT INTO users(name,username,email) VALUES (%s,%s,%s)
        ''', (name, username, email)
    )

for post in posts:
    title = post['title']
    body = post['body']
    user_id = post['userId']
    cursor.execute(
        '''
        INSERT INTO posts(title,body,user_id) VALUES (%s,%s,%s)
        ''', (title, body, user_id)
    )
db.commit()
db.close()
