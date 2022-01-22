import sqlite3

db = sqlite3.connect('translatorBot.db', check_same_thread=False)  # использование нескольких потоков
cursor = db.cursor()
TOKEN = '5073095120:AAFXNLae_qbsqcWkCGFJuzwab4waX98ohhA'
# TOKEN = '5007627528:AAGYWRKaXMkvKfjQBDOYH49KtnQqF7y_E9c'  # нодирники
