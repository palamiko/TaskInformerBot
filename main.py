import threading

from api.bot_api import bot


def main():
    thread_bot = threading.Thread(target=bot.infinity_polling, name='ThreadTelegramBot', daemon=True)
    thread_bot.start()
    thread_bot.join()


if __name__ == '__main__':
    main()
