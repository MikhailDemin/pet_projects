import telebot
from config import TOKEN_API
from worker import get_weather
from worker import get_time

from telebot import types
token = TOKEN_API

city = ''

def get_buttons():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Погода")
    item2 = types.KeyboardButton("Флуд")
    item3 = types.KeyboardButton("Время")
    item4 = types.KeyboardButton("Медицина")
    markup.add(item1, item2)
    markup.add(item3, item4)
    return markup

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,'Привет!')
    bot.send_message(message.chat.id, 'Привет! Выберите тему', reply_markup=get_buttons())

@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text=="Погода":
        bot.send_message(message.chat.id,"Введите город")
        bot.register_next_step_handler(message, weather_reply)
    elif message.text == "Флуд":
        bot.send_message(message.chat.id, "Давайте переговорим")
    elif message.text=="Время":
        bot.send_message(message.chat.id,"Введите город")
        bot.register_next_step_handler(message, time_reply)
    elif message.text=="Медицина":
        bot.send_message(message.chat.id,"Медицина")

def weather_reply(message):
    global city
    city = message.text
    bot.send_message(message.chat.id, str(get_weather(city)))
    bot.send_message(message.chat.id, 'Выберите тему', reply_markup=get_buttons())

def time_reply(message):
    global city
    city = message.text
    bot.send_message(message.chat.id, str(get_time(city)))
    bot.send_message(message.chat.id, 'Выберите тему', reply_markup=get_buttons())


if __name__ == "__main__":
    bot.infinity_polling()