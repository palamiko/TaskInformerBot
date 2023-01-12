import argparse
import logging
import os


def count_default(count: int) -> int:
    if not os.environ["COUNT"]:
        return count
    else:
        return int(os.environ["COUNT"])


def interval_default(interval: int) -> int:
    if not os.environ["INTERVAL"]:
        return interval
    else:
        return int(os.environ["INTERVAL"])


def jira_url(count_task: int) -> str:
    return 'https://support.ai-mark.info/rest/api/2/search?jql=order+by+created' \
           f'&fields=id,key,description,priority,summary,status,creator,customfield_10002&maxResults={count_task}'


parser = argparse.ArgumentParser(description="Arguments for JiraTelegramBotInformer",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-t", "--token", help="token telegram bot", type=str, default=os.environ["TOKEN"])
parser.add_argument("-l", "--login", help="login in jira", type=str, default=os.environ["LOGIN"])
parser.add_argument("-p", "--password", help="password in jira", type=str, default=os.environ["PASSWORD"])
parser.add_argument('-c', "--count", help="max count show tasks", type=int, default=count_default(4))
parser.add_argument('-i', '--interval', help='interview jira about new ticket', type=int, default=interval_default(50))
parser.add_argument('-ll', '--log-level', help='log level [DEBUG, INFO, WARN, ERROR, CRITICAL]', type=str,
                    default=logging.DEBUG)

args = parser.parse_args()
config = vars(args)
