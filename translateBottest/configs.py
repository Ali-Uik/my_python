import sqlite3

db = sqlite3.connect('bot.db', check_same_thread=False)

cursor = db.cursor()

TOKEN = '5075726291:AAHKKfVe8b0qrfJIWRtEQ_kdSkbwBEOz3AI'