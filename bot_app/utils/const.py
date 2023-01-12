from bot_app.utils.config import config, jira_url

TOKEN = config.get('token')  # token бота
LOGIN = config.get('login')
PASSWD = config.get('password')
INTERVAL = config.get('interval')
COUNT = config.get('count')
LOG_LEVEL = config.get('log-level')

GET_URL_JIRA = jira_url
COUNT_TASK_IN_NOTIFY = 1

hello_text = 'Commands' \
             '\n/s - Start' \
             '\n/h - Help, this message' \
             '\n/t - Show last task'

mess_notify_on = 'Уведомления о новых тикетах включены'
mess_notify_off = 'Уведомления о новых тикетах отключены'
name_task_mask = 'SUP-\d{4}'
title_show_ticket = 'Показать тикеты'
