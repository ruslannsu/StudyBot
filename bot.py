import telebot
import config
from openai import OpenAI

from config import API_KEY

client = OpenAI(
    api_key=API_KEY,
    base_url="https://api.vsegpt.ru/v1",
)



bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет, это бот проверяющий твои сочинения на соотвествие критериям ФИПИ")



@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "Это раздел справочной информации")


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    prompt = message.text

    messages = []
    messages.append({"role": "user", "content": prompt})
    response_big = client.chat.completions.create(
        model="anthropic/claude-3-haiku",
        messages=messages,
        temperature=0.7,
        n=1,
        max_tokens=3000,
        extra_headers={"X-Title": "My App"},
    )
    response = response_big.choices[0].message.content
    bot.reply_to(message, response)

bot.polling(none_stop=True)
