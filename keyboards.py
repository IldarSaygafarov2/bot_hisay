from telebot import types


def contact_menu():
    kb = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    kb.row(
        types.KeyboardButton(text="Отправить контакт", request_contact=True)
    )
    return kb