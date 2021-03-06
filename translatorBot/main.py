from configs import *
from telebot import TeleBot
from googletrans import Translator  # google
# from translate import Translator  # microsoft
from keyboards import *
import requests
from bs4 import BeautifulSoup

bot = TeleBot(TOKEN,
              parse_mode='HTML')  # ботни регистрация килдик, parse_mode='HTML' - html тегларни ишлатишга рухсат беради.


@bot.message_handler(commands=['start', 'help', 'history'])  # start, help, history командаларига жавобан ишлайди
def command_start(message):  # message бу - ботдан фойдаланувчи киритган маълумотлар.
    # Унда фойдаланувчи хакидаги маълумотлар ва фойдаланувчи жунатган матн ва бошка куплаб маълумотлар булади
    # {'content_type': 'text', 'id': 280, 'message_id': 280,
    # 'from_user':
    #   {'id': 86199576,
    #   'is_bot': False,
    #   'first_name': 'Иззатбек',
    #   'username': 'abu_Ali_ibn_Rustam',
    #   'last_name': 'Балтаев',
    #   'language_code': 'ru',
    #   'can_join_groups': None,
    #   'can_read_all_group_messages': None,
    #   'supports_inline_queries': None},
    #   'date': 1642569605,
    #   'chat':
    #       {'id': 86199576, 'type': 'private',
    #       'title': None, 'username': 'abu_Ali_ibn_Rustam',
    #       'first_name': 'Иззатбек',
    #       'last_name': 'Балтаев',
    #       'photo': None,
    #       'bio': None,
    #       'has_private_forwards': None,
    #       'description': None,
    #       'invite_link': None,
    #       'pinned_message': None,
    #       'permissions': None,
    #       'slow_mode_delay': None,
    #       'message_auto_delete_time': None,
    #       'has_protected_content': None,
    #       'sticker_set_name': None,
    #       'can_set_sticker_set': None,
    #       'linked_chat_id': None,
    #       'location': None},
    #   'sender_chat': None,
    #   'forward_from': None,
    #   'forward_from_chat': None,
    #   'forward_from_message_id': None,
    #   'forward_signature': None,
    #   'forward_sender_name': None,
    #   'forward_date': None,
    #   'is_automatic_forward': None,
    #   'reply_to_message': None,
    #   'via_bot': None,
    #   'edit_date': None,
    #   'has_protected_content': None,
    #   'media_group_id': None,
    #   'author_signature': None,
    #   'text': '/start',
    #   'entities': [<telebot.types.MessageEntity object at 0x00000293786DC820>],
    #   'caption_entities': None,
    #   'audio': None,
    #   'document': None,
    #   'photo': None,
    #   'sticker': None,
    #   'video': None,
    #   'video_note': None,
    #   'voice': None,
    #   'caption': None,
    #   'contact': None,
    #   'location': None,
    #   'venue': None,
    #   'animation': None,
    #   'dice': None,
    #   'new_chat_member': None,
    #   'new_chat_members': None,
    #   'left_chat_member': None,
    #   'new_chat_title': None,
    #   'new_chat_photo': None,
    #   'delete_chat_photo': None,
    #   'group_chat_created': None,
    #   'supergroup_chat_created': None,
    #   'channel_chat_created': None,
    #   'migrate_to_chat_id': None,
    #   'migrate_from_chat_id': None,
    #   'pinned_message': None,
    #   'invoice': None,
    #   'successful_payment': None,
    #   'connected_website': None,
    #   'reply_markup': None,
    #   'json':
    #       {'message_id': 280,
    #       'from':
    #           {'id': 86199576,
    #           'is_bot': False,
    #           'first_name': 'Иззатбек',
    #           'last_name': 'Балтаев',
    #           'username': 'abu_Ali_ibn_Rustam',
    #           'language_code': 'ru'},
    #       'chat':
    #           {'id': 86199576,
    #           'first_name': 'Иззатбек',
    #           'last_name': 'Балтаев',
    #           'username': 'abu_Ali_ibn_Rustam',
    #           'type': 'private'},
    #       'date': 1642569605,
    #       'text': '/start',
    #       'entities': [{'offset': 0, 'length': 6, 'type': 'bot_command'}]}}
    chat_id = message.chat.id
    # chat_id = message.chat.id бу- хар бир тг фойдаланувчиси учун укикал булган сонли комбинация
    if message.text == '/start':
        msg = bot.send_message(chat_id,  # ботдан фойдаланувчига жунатиладиган маълумотлар
                               f'''Привет <b>{message.from_user.first_name}</b>. Я бот перевода и определения слов и текста.''',
                               reply_markup=generate_phone_number())
        cursor.execute('''SELECT * FROM users WHERE telegram_id = ?;''', (chat_id,))
        user = cursor.fetchone()
        if user:
            bot.send_message(chat_id, 'Что желаете сделать?', reply_markup=choose_command())
        else:
            bot.register_next_step_handler(msg, register_user)
        # TODO сделать функцию регистраци
    elif message.text == '/help':
        bot.send_message(chat_id,
                         f'''Этот бот создал <b>И.Б.Рустамбоевич</b>. Бот работает в тестовом режиме. Если у вас ест вопросы пишите сюда: @abu_Ali_ibn_Rustam''')
    elif message.text == '/history':
        chat_id = message.chat.id
        cursor.execute('''
        SELECT user_text, translate_text
        FROM history_translation JOIN users
        ON history_translation.user_id = users.user_id
        WHERE telegram_id=?;
        ''', (chat_id,))
        history_list = cursor.fetchall()
        db.commit()
        for msg in history_list:
            bot.send_message(chat_id, f'Ваша история:{msg} ')


def register_user(message):
    chat_id = message.chat.id
    try:
        first_name = message.from_user.first_name
        user_name = message.from_user.username
        phone = message.contact.phone_number
        cursor.execute('''
        INSERT INTO users(telegram_id,first_name,user_name,phone) VALUES
        (?,?,?,?); 
        ''', (chat_id, first_name, user_name, phone))
        db.commit()
        msg = bot.send_message(chat_id, 'Что желаете сделать?', reply_markup=choose_command())
    except:
        msg = bot.send_message(chat_id, 'Нажмите на кнопку!!!', reply_markup=generate_phone_number())
        bot.register_next_step_handler(msg, register_user)


@bot.message_handler(regexp=r'Перевод \U0001F504')  # regexp
def translate_start(message):
    chat_id = message.chat.id
    word = bot.send_message(chat_id, 'Введите слово или текст, которые хотите перевести.')
    bot.register_next_step_handler(word, translation)


@bot.message_handler(regexp=r'Определение \U0001F4DD')
def definition_start(message):
    chat_id = message.chat.id
    word = bot.send_message(chat_id, 'Введите слово, определение которого хотите знать.')
    bot.register_next_step_handler(word, wikipedia_answer)


def translation(message):
    chat_id = message.chat.id
    word = message.text
    print(word)
    if word in ['Определение \U0001F4DD', '/start', '/help', '/history']:
        if word == 'Определение \U0001F4DD':
            definition_start(message)
        else:
            command_start()
    else:
        # translator = Translator(from_lang='ru', to_lang='en')
        translator = Translator()
        english_word = translator.translate(text=word, dest='en')
        # english_word = translator.translate(word)
        english_word_text = english_word.text
        print(english_word_text)
        cursor.execute('''
        SELECT user_id FROM users WHERE telegram_id = ?;
        ''', (chat_id,))
        user_id = cursor.fetchone()[0]
        cursor.execute('''
        INSERT INTO history_translation (user_id,user_text,translate_text) VALUES (?,?,?);
        ''', (user_id, word, english_word_text))
        db.commit()
        bot.send_message(chat_id, english_word_text)
        translate_start(message)
        # msg = bot.send_message(chat_id, 'Что желаете сделать?', reply_markup=choose_command())


# def wikipedia_answer(message):
#     word = message.text
#     chat_id = message.chat.id
#     if word in ['Перевод \U0001F504', 'Определение \U0001F4DD', '/start', '/help', '/history']:
#         if word == 'Перевод \U0001F504':
#             translate_start(message)
#         else:
#             command_start(message)
#     else:
#         full_url = f'https://ru.wikipedia.org/wiki/{word}'
#         print(full_url)
#         html = requests.get(full_url).text
#         soup = BeautifulSoup(html, 'html.parser')
#         definition = soup.find('p').get_text(strip=True)
#         print(definition)
#         cursor.execute('''
#                 SELECT user_id FROM users WHERE telegram_id = ?;
#                 ''', (chat_id,))
#         user_id = cursor.fetchone()[0]
#         cursor.execute('''
#                 INSERT INTO history_definition (user_id,user_text,definition_text) VALUES (?,?,?);
#                 ''', (user_id, word, definition))
#         db.commit()
#         bot.send_message(chat_id, definition)
#         definition_start(message)


bot.polling(none_stop=True)  # ботнинг тухтамасдан ишлаши учун
