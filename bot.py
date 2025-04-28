import telebot


from openai import OpenAI

import config

import os

from dotenv import load_dotenv

from config import PROMT_HEADER

load_dotenv()

API_KEY = os.getenv("API_KEY")

TOKEN = os.getenv("TOKEN")


client = OpenAI(
    api_key=API_KEY,
    base_url="https://api.vsegpt.ru/v1",
)

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет, это бот проверяющий твои сочинения на соотвествие критериям ФИПИ")

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "Это раздел справочной информации")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    prompt = config.PROMT_HEADER + message.text
    messages = []
    messages.append({"role": "user", "content": prompt})
    response_big = client.chat.completions.create(
        model="google/gemini-2.5-flash-pre",
        messages=messages,
        temperature=0.7,
        n=1,
        max_tokens=1500,
        extra_headers={"X-Title": "My App"},
    )
    response = response_big.choices[0].message.content
    bot.reply_to(message, response)

bot.polling(none_stop=True)
