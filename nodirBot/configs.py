import sqlite3

db = sqlite3.connect('bot.db', check_same_thread=False)

cursor = db.cursor()
TOKEN = '5007627528:AAGYWRKaXMkvKfjQBDOYH49KtnQqF7y_E9c'