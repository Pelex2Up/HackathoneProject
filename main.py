import telebot

bot = telebot.TeleBot("5621023291:AAHMLhmpOOEpA1XRtRWebijBmsYms4neYSA")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, """Добрый день, {0.first_name}! Вас приветствует служба поддержки пользователей.
Чем я могу Вам помочь?""".format(message.from_user))

@bot.message_handler(func=lambda message: True)
def user_request(message):
	bot.reply_to(message, 'Ваш запрос принят. Ожидайте ответ от службы поддержки!')

bot.polling(none_stop=True, interval=0)