import requests

from bot_app import logger
from bot_app.utils.const import GET_URL_JIRA, LOGIN, PASSWD


class JiraApi:

    def __init__(self, login, passwd):
        self.session = requests.Session()
        self.session.auth = (login, passwd)

    def get_tasks(self, count_task: int) -> dict:
        url = GET_URL_JIRA(count_task)

        try:
            logger.info('Request to Jira')
            response = self.session.get(url).json()

            logger.info('Answer from Jira received')
            logger.debug(f'Answer from Jira received. Body answer: {response}')

            return response

        except requests.exceptions.RequestException as ex:
            logger.critical(ex)
            logger.exception(ex)


jira_api = JiraApi(LOGIN, PASSWD)
