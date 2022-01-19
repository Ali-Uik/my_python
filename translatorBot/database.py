from configs import *
cursor.executescript(
    # executescript - это нестандартный удобный метод для одновременного выполнения нескольких операторов SQL.
    '''
    DROP TABLE IF EXISTS users;
    CREATE TABLE IF NOT EXISTS users(
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        telegram_id INTEGER,
        first_name TEXT,
        user_name TEXT,
        phone TEXT 
    );
    DROP TABLE IF EXISTS history_translation;
    CREATE TABLE IF NOT EXISTS history_translation(
        translation_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER REFERENCES users(user_id),   
        user_text TEXT,
        translate_text TEXT
    );
    DROP TABLE IF EXISTS history_definition;
    CREATE TABLE IF NOT EXISTS history_definition(
        definition_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER REFERENCES users(user_id),   -- REFERENCES бу - богликлик
        user_text TEXT,
        definition_text TEXT
    );
    ''')

db.commit()
db.close()