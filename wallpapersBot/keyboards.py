from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


def generate_categories(categories):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    buttons = []
    for category in categories:
        btn = KeyboardButton(text=category[0])
        buttons.append(btn)
    markup.add(*buttons)
    return markup
