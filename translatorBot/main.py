from configs import *
from telebot import TeleBot
from googletrans import Translator
from pprint import pprint
from keyboards import *

bot = TeleBot(TOKEN)  # ботни регистрация килдик


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
        bot.send_message(chat_id,  # ботдан фойдаланувчига жунатиладиган маълумотлар
                         f'''Привет {message.from_user.first_name}. Я бот перевода и определения слов и текста.''', reply_markup=generate_phone_number())
    elif message.text == '/help':
        bot.send_message(chat_id,
                         f'''Этот бот создал И.Б.Рустамбоевич. Бот работает в тестовом режиме. Если у вас ест вопросы пишите сюда: @abu_Ali_ibn_Rustam''')
    elif message.text == '/history':
        bot.send_message(chat_id, 'Ваша история: ')


bot.polling(none_stop=True)  # ботнинг тухтамасдан ишлаши учун
