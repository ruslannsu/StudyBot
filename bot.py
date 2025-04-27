import telebot

import config

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет, это бот проверяющий твои сочинения на соотвествие критериям ФИПИ")



@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "Это раздел справочной информации")

bot.polling(none_stop=True)
