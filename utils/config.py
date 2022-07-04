import argparse

parser = argparse.ArgumentParser(description="Arguments for JiraTelegramBotInformer",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-t", "--token", help="token telegram bot", type=str)
parser.add_argument("-l", "--login", help="login in jira", type=str)
parser.add_argument("-p", "--password", help="password in jira", type=str)
parser.add_argument('-c', "--count", help="max count show tasks", type=int, default=4)
parser.add_argument('-i', '--interval', help='interview jira about new ticket', type=int, default=50)

args = parser.parse_args()
config = vars(args)

TOKEN = config.get('token')  # token бота
LOGIN = config.get('login')
PASSWD = config.get('password')
INTERVAL = config.get('interval')
COUNT = config.get('count')

GET_TASKS_JIRA = 'https://jira.crpt.ru/rest/api/2/search?jql=project=EASUP+order+by+created' \
                 '&fields=id,key,description,priority,customfield_11611,summary,status,customfield_11213' \
                 f',assignee.displayName,customfield_12838&maxResults={COUNT}'
