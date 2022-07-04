from models.tasks import PrevTask, Task
from utils.const import title_show_ticket


class MessageHandler:

    message = None

    def __init__(self):
        self.temp_task: list[PrevTask] = []

    @classmethod
    def _get_executor(cls, data):
        """ Получает имя исполнителя при его наличии иначе - """

        try:
            return data.fields.assignee.displayName
        except AttributeError:
            return '-'

    def write_temp_data(self, data: list[PrevTask]):
        """ Кеширует полученные тикеты для обращений к ним в дальнейшем """

        self.temp_task.clear()
        self.temp_task.extend(data)

    def get_task_from_json(self, json_obj: dict) -> list[PrevTask]:
        """ Формирует список PrevTask из json(полученный из jira)  """
        formed_tasks = []
        raw_tasks: list[dict] = json_obj['issues']

        for i in raw_tasks:
            raw_task = Task.from_dict(i)
            task = PrevTask(
                key=raw_task.key,
                title=raw_task.fields.summary,
                country=raw_task.fields.customfield_12838.value,
                executor=self._get_executor(raw_task),
                contact=raw_task.fields.customfield_11611,
                status=raw_task.fields.status.name,
                solution=raw_task.fields.status.statusCategory.name,
                priority=raw_task.fields.priority.name,
                number=raw_task.fields.customfield_11213,
                description=raw_task.fields.description
            )
            formed_tasks.append(task)

        return formed_tasks

    def get_task_from_list(self, task_list: list[Task]) -> list[PrevTask]:
        """ Формирует список PrevTask из списка """
        formed_tasks = []

        for task in task_list:
            task = PrevTask(
                key=task.key,
                title=task.fields.summary,
                country=task.fields.customfield_12838.value,
                executor=self._get_executor(task),
                contact=task.fields.customfield_11611,
                status=task.fields.status.name,
                solution=task.fields.status.statusCategory.name,
                priority=task.fields.priority.name,
                number=task.fields.customfield_11213,
                description=task.fields.description
            )
            formed_tasks.append(task)

        return formed_tasks

    @classmethod
    def format_message(cls, items: list[PrevTask]) -> str:
        """  Формирует читабельный вывод краткого списка тикетов"""

        string_msg = ''
        for task in items:
            foo = f'<b>Код</b>: {task.key}\n' \
                  f'<b>Тема</b>: {task.title}\n' \
                  f'<b>Страна</b>: {task.country}\n' \
                  f'<b>Контакт</b>: {task.contact}\n' \
                  f'<b>Приоритет</b>: {task.priority}\n' \
                  f'<b>Статус</b>: {task.status}\n' \
                  f'<b>Решение</b>: {task.solution}\n' \
                  f'<b>Номер</b>: {task.number}\n\n'
            string_msg += foo
        return string_msg

    @classmethod
    def unpack_task_key(cls, tasks: list[PrevTask]) -> list[str]:
        """ Формирует список имен(EASUP-xxx) тикетов для названий кнопок """
        task_keys = [title_show_ticket]
        for item in tasks:
            task_keys.append(item.key)
        return task_keys


mess_handler = MessageHandler()
