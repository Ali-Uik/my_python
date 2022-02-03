from configs import *

cursor.executescript('''
    DROP TABLE IF EXISTS users;
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        chat_id INTEGER,
        db_id INTEGER,
        user_name TEXT    
    );
    DROP TABLE IF EXISTS main_table;
    CREATE TABLE IF NOT EXISTS main_table(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        db_id INTEGER REFERENCES users(db_id),
        bomdod INTEGER,
        peshin INTEGER,
        asr INTEGER,
        shom INTEGER,
        xufton INTEGER,
        vitr INTEGER
    );
''')

db.commit()
db.close()
