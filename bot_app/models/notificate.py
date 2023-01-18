import collections
import threading
import time
from typing import Any

from bot_app import logger
from bot_app.api.jira_api import JiraApi, jira_api

from bot_app.models.message_handler import MessageHandler, mess_handler
from bot_app.models.tasks import Task

from bot_app.utils.const import COUNT_TASK_IN_NOTIFY, INTERVAL


def compare(list_old, list_new) -> bool:
    return collections.Counter(list_old) == collections.Counter(list_new)


def create_list_names(tasks: list[Task]):
    return list(map(lambda x: x.key, tasks))


class NotificationsAboutNewTask:

    def __init__(self, interval: int, _jira_api: JiraApi, message_handler: MessageHandler):
        self.interval = interval
        self.jira_api = _jira_api
        self.message_handler = message_handler
        self.last_state = self.get_task_from_jira()
        self.notify: bool = True  # Уведомления вкл/откл

    def get_task_from_jira(self) -> list[Task]:
        """ Формирует список Task из json(полученный из jira) """

        formed_tasks = []
        json_obj = self.jira_api.get_tasks(COUNT_TASK_IN_NOTIFY)

        if json_obj is not None:
            raw_tasks: list[dict] = json_obj['issues']

            for i in raw_tasks:
                formed_tasks.append(Task.from_dict(i))
        else:
            formed_tasks.extend(notification.last_state)

        return formed_tasks

    def sent_notification(self, equals: bool, tasks: list[Task]):
        """ Отправляет уведомление если свойство equals=false, то есть списки разные """

        from bot_app.api.bot_api import send_notification

        logger.debug(f'Тикеты одинаковые: {equals}')
        print(f'Тикеты одинаковые: {equals}')
        if not equals:
            logger.debug('New task found')

            list_prev = self.message_handler.get_task_from_list(tasks)
            notify_text = self.message_handler.format_message(list_prev)
            send_notification(message=mess_handler.message, notify_text=notify_text)

            self.write_last_state(tasks=tasks)

    def write_last_state(self, tasks: list[Task]):
        self.last_state.clear()
        self.last_state.extend(tasks)

    @staticmethod
    def run_thread(function: Any):
        """ Запускает поток с уведомлениями о новых тикетах """

        thread_notify = threading.Thread(target=function, name='ThreadNotificationAboutNewTask', daemon=True)
        thread_notify.start()
        thread_notify.join()

    def run_observer(self):
        """ Проверяет с периодичностью наличие новых обращений если включены уведомления """

        while True:
            time.sleep(self.interval)

            if self.notify:
                tasks = self.get_task_from_jira()
                equal = compare(
                    list_old=create_list_names(self.last_state),
                    list_new=create_list_names(tasks)
                )

                self.sent_notification(equals=equal, tasks=tasks)


notification = NotificationsAboutNewTask(interval=INTERVAL, _jira_api=jira_api, message_handler=mess_handler)
