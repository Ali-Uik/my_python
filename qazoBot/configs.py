import sqlite3

db = sqlite3.connect('qazoBotmain.db', check_same_thread=False)  # использование нескольких потоков
cursor = db.cursor()
TOKEN = '5158166587:AAH6v2bJLOPuYmTqyvmWTiEqnV_Dcgu9IgE'  # @ali_uik_testbot


