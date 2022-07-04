import telebot
from telebot import types

from api.jira_api import jira_api

from models.notificate import notification
from utils.config import TOKEN
from models.message_handler import mess_handler
from utils.const import *

bot = telebot.TeleBot(TOKEN, parse_mode='html')


def add_btn_get_task(message):
    """ Добавляет кнопку 'Показать тикеты' """

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    show_ticket = types.KeyboardButton(title_show_ticket)
    markup.add(show_ticket)
    bot.reply_to(message, 'main menu', reply_markup=markup)


def add_btn_get_task_desc(message, arg):
    """ Добавляет кнопки с именами тикетов для просмотра подробной информации """

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(*arg)
    bot.reply_to(message, 'ticket menu', reply_markup=markup)


def send_notification(notify_text: str):
    """ Оправляет любое уведомление """

    bot.send_message(mess_handler.message.chat.id, notify_text)
    # bot.reply_to(message=mess_handler.message, text=notify_text)


@bot.message_handler(commands=['start', 's', 'h'])
def start(message):
    mess_handler.message = message

    send_notification(hello_text)
    add_btn_get_task(message)


@bot.message_handler(commands=['on'])
def notification_on(message):

    notification.notify = True
    send_notification(mess_notify_on)
    notification.run_thread()


@bot.message_handler(commands=['off'])
def notification_off(message):

    notification.notify = False
    send_notification(mess_notify_off)


@bot.message_handler(regexp=name_task_mask)
def send_task_desc(message):
    """ Отправляет подробное описание одной заявки """

    for item in mess_handler.temp_task:
        if item.key == message.text:
            send_notification(item.description)


@bot.message_handler(content_types=['text'])
def text_input_handler(message):
    if message.text in [title_show_ticket, 't']:
        # Отправляет краткое описание 4‑х последних тикетов

        tasks = mess_handler.get_task_from_json(jira_api.get_four_task())
        bot.reply_to(message, mess_handler.format_message(tasks))

        add_btn_get_task_desc(message, arg=mess_handler.unpack_task_key(tasks))
        mess_handler.write_temp_data(tasks)
