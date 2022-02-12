import sqlite3

db = sqlite3.connect('qazoBotmain.db')
cursor = db.cursor()
cursor.execute('''

        INSERT INTO users(chat_id,db_id,user_name)
        VALUES
        (1,4,'ALI'),
        (2,8,'BONU');

    ''')
cursor.execute('''SELECT * FROM users;''')
data = cursor.fetchall()
print(data)
db.commit()
db.close()
