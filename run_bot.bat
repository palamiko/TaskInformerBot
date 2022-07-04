
@set token="token"
@set login="login"
@set password="password"
@set count=4
@set interval=40

echo "Bot started.."

@python ./main.py -t %token% -l %login% -p %password% -c %count% -i %interval%
pause