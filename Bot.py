import telebot
from Info import about_me, projects
from telebot import types
from peremen import *


bot = telebot.TeleBot(token=token)


#Комманды
@bot.message_handler(commands=['start', 'help', 'about'])
def handle_command(message):
    keyboard = telebot.types.ReplyKeyboardMarkup()
    item1 = telebot.types.KeyboardButton("/start")
    item2 = telebot.types.KeyboardButton("/help")
    item3 = telebot.types.KeyboardButton("/about")
    keyboard.add(item1, item2, item3)
    msg = bot.send_message(message.chat.id, 'Выберите кнопку:', reply_markup=keyboard)
    if message.text == '/start':
        bot.reply_to(message, "Привет! Я личный бот-визитка Князева Ивана.\n"
                              "Для того чтобы узнать что я могу используйте комманду /help")

    elif message.text == "/help":
        bot.reply_to(message, "/start - запускает бота\n"
                              "/help - выводит справку о возможностях бота\n"
                              "/about - выводит информацию обо мне (Создателе бота).\n"
                              "\n"
                              "Также я могу отвечать на некоторые сообщение, такие как:\n"
                              "Привет, Пока, Как тебя зовут ? и Что ты умеешь ?\n"
                              "")
    elif message.text == "/about":
        bot.reply_to(message, "Вот что можно узнать обо мне :\n"
                              "\n"
                              f"Имя и Фамилия: {about_me['my_name']}\n"
                              "\n"
                              f"Возраст: {about_me['age']}\n"
                              "\n"
                              f"Мои хобби: \n"
                              f"{about_me['hobby'][0]}\n"
                              f"{about_me['hobby'][1]}\n"
                              f"{about_me['hobby'][2]}\n"
                              f"{about_me['hobby'][3]}\n"
                              f"{about_me['hobby'][4]}\n"
                              f"\n"
                              f"Моя почта : {about_me['email']}\n"
                              f"\n"
                              f"Также у меня есть несколько проектов, такие как:\n"
                              f"1.) {projects[1]}\n"
                              f"2.) {projects[2]}\n"
                              f"3.) {projects[3]}\n"
                              f"4.) {projects[4]}\n")


#Ответы на некоторые текстовые и фото запросы
def filter_password(message):
    password = "привет"
    return password in message.text.lower()

@bot.message_handler(content_types=['text'], func =filter_password)
def say_hello(message):
    bot.send_message(message.chat.id, "Здравствуйте !")


def filter_password_bue(message):
    password = "пока"
    return password in message.text.lower() or "до свидания" in message.text.lower()

@bot.message_handler(content_types=['text'], func =filter_password_bue)
def say_bue(message):
      bot.send_message(message.chat.id, "До свидания !")


def filter_password_what(message):
    password = "какие команды у тебя есть"
    return password in message.text.lower() or "что ты умеешь" in message.text.lower()

@bot.message_handler(content_types=['text'], func =filter_password_what)
def say_comm(message):
      bot.send_message(message.chat.id, "Это можно узнать через команду /help")


def filter_password_name(message):
    password = "как тебя зовут"
    return password in message.text.lower() or "что ты такое" in message.text.lower()

@bot.message_handler(content_types=['text'], func =filter_password_name)
def say_name(message):
      bot.send_message(message.chat.id, "Меня зовут Popuga, бот-визитка, а про мои функции ты можешь узнать через команду /help")


@bot.message_handler(content_types=['text'])
def say_what(message):
     bot.send_message(message.chat.id, "Не очень понял, но  вы можете узнать что я могу через команду /help")



@bot.message_handler(content_types=['photo'])
def say_photo(message):
     bot.send_message(message.chat.id, message.photo)



bot.polling()