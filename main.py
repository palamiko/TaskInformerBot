import threading

from bot_app import logger
from bot_app.api.bot_api import bot


def main():
    try:
        thread_bot = threading.Thread(target=bot.infinity_polling, name='ThreadTelegramBot', daemon=True)
        thread_bot.start()
        thread_bot.join()
    except Exception as ex:
        # logger.exception(ex)
        logger.critical(ex)


if __name__ == '__main__':
    main()
