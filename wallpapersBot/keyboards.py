from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


def generate_categories(categories):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    buttons = []
    for category in categories:
        btn = KeyboardButton(text=category[0])
        buttons.append(btn)
    markup.add(*buttons)
    return markup


def download_button(image_id):
    markup = InlineKeyboardMarkup()
    download = InlineKeyboardButton(text='Скачать в максимальном качестве', callback_data=f'Download_{image_id}')
    markup.add(download)
    return markup

