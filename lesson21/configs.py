import sqlite3
db = sqlite3.connect('bot.db', check_same_thread=False)
cursor = db.cursor()
