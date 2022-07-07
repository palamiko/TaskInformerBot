@set token="token"
@set login="login"
@set password="pass"
@set count=4
@set interval=40
@set LOG_CFG=.\bot_app\utils\log_config.yaml

@python ./main.py -t %token% -l %login% -p %password% -c %count% -i %interval%
pause