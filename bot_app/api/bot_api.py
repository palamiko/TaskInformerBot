import telebot
from telebot import types

from bot_app import logger
from bot_app.api.jira_api import jira_api

from bot_app.models.message_handler import mess_handler
from bot_app.models.notificate import notification
from bot_app.utils.const import *


bot = telebot.TeleBot(TOKEN, parse_mode='html')


def add_btn_get_task(message):
    """ Добавляет кнопку 'Показать тикеты' """

    logger.info('add btn: "Show Tasks"')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    show_ticket = types.KeyboardButton(title_show_ticket)
    markup.add(show_ticket)
    bot.reply_to(message, 'main menu', reply_markup=markup)


def add_btn_get_task_desc(message, arg):
    """ Добавляет кнопки с именами тикетов для просмотра подробной информации """

    logger.info('add btn: "Ticket name"')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(*arg)
    bot.reply_to(message, 'ticket menu', reply_markup=markup)


def send_notification(message, notify_text: str):
    """ Оправляет любое уведомление """

    logger.debug(f'command: send_notification. notification text:{notify_text}')
    bot.send_message(message.chat.id, notify_text)
    #  bot.reply_to(message=mess_handler.message, text=notify_text)


@bot.message_handler(commands=['start', 's', 'h'])
def start(message):
    logger.debug('command: start')

    send_notification(message, notify_text=hello_text)
    add_btn_get_task(message)


@bot.message_handler(commands=['on'])
def notification_on(message):
    logger.debug('command: notification_on')

    mess_handler.message = message
    notification.notify = True
    send_notification(message, notify_text=mess_notify_on)
    notification.run_thread()


@bot.message_handler(commands=['off'])
def notification_off(message):
    logger.debug('command: notification_off')

    notification.notify = False
    send_notification(message, notify_text=mess_notify_off)


@bot.message_handler(regexp=name_task_mask)
def send_task_desc(message):
    """ Отправляет подробное описание одной заявки """
    logger.debug(f'command: description {message.text}')

    for item in mess_handler.temp_task:
        if item.key == message.text:
            send_notification(message, notify_text=item.description)


@bot.message_handler(content_types=['text'])
def text_request_handler(message):
    logger.debug('command: show_tickets')

    if message.text in [title_show_ticket, 't']:
        # Отправляет краткое описание 4‑х последних тикетов

        tasks = mess_handler.get_task_from_json(jira_api.get_tasks(COUNT))
        bot.reply_to(message, mess_handler.format_message(tasks))

        add_btn_get_task_desc(message, arg=mess_handler.unpack_task_key(tasks))
        mess_handler.write_temp_data(tasks)
