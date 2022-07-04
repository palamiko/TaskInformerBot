import requests

from utils.config import GET_TASKS_JIRA, LOGIN, PASSWD


class JiraApi:

    def __init__(self, login, passwd):
        self.session = requests.Session()
        self.session.auth = (login, passwd)

    def get_four_task(self, url=GET_TASKS_JIRA) -> dict:
        try:
            return self.session.get(url).json()

        except requests.exceptions.RequestException as ex:
            print(ex)


jira_api = JiraApi(LOGIN, PASSWD)
