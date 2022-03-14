import sqlite3

db = sqlite3.connect('qazoBotmain.db')
cursor = db.cursor()
# print(cursor)
cursor.execute('''

        INSERT INTO users(chat_id,db_id,user_name)
        VALUES
        (3,5,'Sabrina'),
        (4,9,'Zara');

    ''')
cursor.execute('''SELECT * FROM users;''')
data = cursor.fetchall()
print(data)
db.commit()
db.close()
