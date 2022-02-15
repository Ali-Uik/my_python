from configs import *
from pprint import pprint


def sign_up_start():
    # chat_id = message.chat.id
    # user_text = message.text
    cursor.execute('''SELECT MAX(id) FROM users;''')
    max_id = cursor.fetchone()
    print(max_id[0])


sign_up_start()
