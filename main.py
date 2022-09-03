import telebot
import json
from telebot import types
from json_data import *

flag_user = False
bot = telebot.TeleBot("5621023291:AAHMLhmpOOEpA1XRtRWebijBmsYms4neYSA")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	button1 = types.KeyboardButton("/authorization")
	markup.add(button1)
	bot.send_message(message.chat.id, """Вас приветствует служба поддержки пользователей.
	Пожалуйста авторизируйтесь.""".format(message.from_user), reply_markup=markup)


@bot.message_handler(commands=['authorization'])
def auth(message):
	global flag_user
	with open("data_users.json", "r") as f:
		check = str(message.from_user.id)
		for line in f:
			if check == line:
				flag_user = True
				bot.send_message(message.chat.id, """Добрый день, {0.first_name}! Вас приветствует служба поддержки пользователей.
		Вы зашли в систему, задавайте вопрос.""".format(message.from_user))
				break
		else:
			bot.send_message(message.chat.id, 'Такой ID в системе не зарегистрирован.')


@bot.message_handler(content_types='text')
def user_request(message):
	global flag_user
	if flag_user == True:
		bot.reply_to(message, 'Ваш запрос принят. Ожидайте ответ от службы поддержки!')
		admin = -1001671702709
		sent = bot.send_message(admin, f'Новый запрос от пользователя @{message.from_user.username}: {message.text}')
		bot.register_next_step_handler(sent, admin_answer)
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		but1 = types.KeyboardButton("Завершить запрос.")
		markup.add(but1)
	else:
		bot.send_message(message.chat.id, 'Вы не прошли авторизацию. Обратитесь к администратору.')


@bot.message_handler(content_types='text')
def admin_answer(message):
	admin = message.from_user.id
	bot.send_message(admin, message.text)

bot.polling(none_stop=True, interval=0)


