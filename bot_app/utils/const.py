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
             '\n/on - Notification about new task on.' \
             '\n/off - Notification about new task off.' \
             '\nt - Show last task'

mess_notify_on = 'Уведомления о новых тикетах включены'
mess_notify_off = 'Уведомления о новых тикетах отключены'
name_task_mask = 'EASUP-\d{3}'
title_show_ticket = 'Показать тикеты'


