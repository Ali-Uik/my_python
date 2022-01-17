from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def generate_phone_number():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn = KeyboardButton(text='Отправьте свой контакт!', request_contact=True)
    markup.add(btn)
    return markup


def choose_command():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    translate = KeyboardButton(text='Перевод \U0001F913')  # U+1F913 == U0001F913
    # https: // unicode.org / emoji / charts / full - emoji - list.html - эможилар руйхати коди билан!!!!!
    definition = KeyboardButton(text='Определение \U0001F9D0')
    markup.add(translate, definition)
    return markup


