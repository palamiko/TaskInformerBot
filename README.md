# JiraTelegramBotInformer

Телеграм бот для просмотра N-ого числа последних заявок в Jira. Выводит по умолчанию 4 последних тикета кратким списком,
после чего добавляются 4 кнопки с номерами тикетов, предоставляющие возможность получить более подробные сведения о 
каждом отдельном обращении.

### Быстрый старт

###### Установка
1. Скопировать репозиторий в удобное место.
2. Далее подразумевается что у Вас установлен [Python 3.8+](https://www.python.org/downloads/release/python-3813/)
и [pip](https://pip.pypa.io/en/stable/installation/). Запустить install.bat, он установит зависимости.
3. Создать своего Telegram Bot. 
* Найти [@BotFather](https://telegram.me/botfather).
* Выполнить /start, затем /newbot.
* Заполнить требующиеся данные и получить bot_token.

###### Запуск
1. В run_bot.bat указать полученный ранее token, а так же login и password от Jira, дополнительно можно указать 
количество получаемых тикетов.
2. Запустить run_bot.bat
3. Найти своего бота по ранее придуманному имени и выполнить /start.

###### Альтернативный запуск
Выполнить _python ./main.py -t token -l login -p password -c count_


### Структура проекта
```
TaskInformerBot
|    install.bat
|    run_bot.bat
|    requirements.txt  #  Зависимости для работы бота
|    readme.md
|    main.py  #  Точка входа в приложение
|
└─── api
|    |    
|    |    bot_api.py  # Предоставляет методы для работы с Telegram.
|    |    jira_api.py  # Предоставляет методы для запросов в Jira.
|    
└─── models
|    |    
|    |    message_handler.py  # Вспомогательный класс для форматирования сообщений на вывод в Telegram.
|    |    tasks.py  # Модель сообщения получаемая от Jira.
|
└─── utils
     |
     |    config.py  # Парсер ключей запуска.

    
```

![bot prev](./preview.png)