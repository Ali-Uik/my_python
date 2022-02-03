from configs import *
from pprint import pprint


def sign_in_start():
    # chat_id = message.chat.id
    # user_text = message.text
    # print(user_text)
    cursor.execute('''SELECT * FROM users;''')
    db_ids = cursor.fetchall()
    db.commit()
    pprint(db_ids)
    # for db_id in db_ids:
    #     if db_id == user_text:
    #         bot.send_message(chat_id, 'Ishladi')
    #     else:
    #         bot.send_message(chat_id, 'Ishlamadi')


sign_in_start()
