from telebot import TeleBot, types

import api
import config
import keyboards

bot = TeleBot(token=config.BOT_TOKEN)


@bot.message_handler(commands=['start'])
def command_start(message: types.Message):
    chat_id = message.chat.id
    msg = """
Здравствуйте, дорогой пользователь.
Вас приветствует бот для регистрации в приложении HiSay
Прошу тебя нажать на кнопку ниже, для дальнейшем регистрации в приложении
"""
    bot.send_message(chat_id, msg, reply_markup=keyboards.contact_menu())


@bot.message_handler(content_types=['contact'])
def check_phone_from_contact(message: types.Message):
    chat_id = message.chat.id
    phone_number = message.contact.phone_number
    username = message.from_user.username
    data = api.save_data_from_bot(
        phone_number=phone_number,
        tg_username=username if username else "No name",
        tg_chat_id=chat_id
    )
    bot.send_message(chat_id, "Ваши данные отправлены, можете продолжить регистрацию в приложении")


if __name__ == '__main__':
    print('BOT STARTED')
    bot.infinity_polling()
