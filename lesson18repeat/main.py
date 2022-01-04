import sqlite3
from pprint import pprint

db = sqlite3.connect('lesson18repeat.db')
cursor = db.cursor()

# Один запрос
# Несколько запросов

# один запрос

# cursor.execute('''
#     SELECT * FROM customers;
# ''')
#
# customers = cursor.fetchall()  # позволит взять все
# pprint(customers)
# # fetchone() - для взятие одного значения

cursor.executescript('''
    DROP TABLE IF EXISTS users;
    CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
    );
''')

# Чтобы отправить данные
db.commit()
db.close()
