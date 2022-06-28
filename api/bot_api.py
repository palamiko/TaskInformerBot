import telebot
from telebot import types

from api.jira_api import jira_api
from utils.config import TOKEN
from models.message_handler import mess_handler

bot = telebot.TeleBot(TOKEN, parse_mode='html')


def add_button_get_task(message):
    """ Добавляет кнопку 'Показать тикеты' """

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    show_ticket = types.KeyboardButton('Показать тикеты')
    markup.add(show_ticket)
    bot.reply_to(message, 'main menu', reply_markup=markup)


def add_button_get_task_desc(message, arg):
    """ Добавляет кнопки с именами тикетов для просмотра подробной информации """

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(*arg)
    bot.reply_to(message, 'ticket menu', reply_markup=markup)


@bot.message_handler(commands=['start'])
def start(message):
    add_button_get_task(message)


@bot.message_handler(commands=['task'])
def send_tasks(self, message):
    """ Не требуется """
    tasks = mess_handler.get_task_from_json(self.jira_api.get_four_task())

    bot.reply_to(message, self.mess_handler.format_message(tasks))
    mess_handler.write_temp_data(tasks)


@bot.message_handler(regexp='EASUP-\d{3}')
def send_task_desc(message):
    """ Отправляет подробное описание одной заявки """

    for item in mess_handler.temp_task:
        if item.key == message.text:
            bot.reply_to(message, item.description)


@bot.message_handler(content_types=['text'])
def send_last_task(message):
    """ Отправляет краткое описание 4х последних тикетов """

    if message.text == "Показать тикеты":
        tasks = mess_handler.get_task_from_json(jira_api.get_four_task())
        bot.reply_to(message, mess_handler.format_message(tasks))

        add_button_get_task_desc(message, arg=mess_handler.unpack_task_key(tasks))
        mess_handler.write_temp_data(tasks)
