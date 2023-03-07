import telebot

API_KEY = "6261270918:AAGOqkikoU6-baL8GRDbriUsxG8J5Ys-ZAk"

bot = telebot.TeleBot(API_KEY)

print('bot Started')


@bot.message_handler(commands=['start', 'hello'])
def send_welcom(message):
    bot.reply_to(message, "Howdy, how are you doing !?")

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.infinity_polling(5)