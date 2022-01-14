from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def generate_phone_number():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn = KeyboardButton(text='Отправьте свой контакт!', request_contact=True)
    markup.add(btn)
    return markup
