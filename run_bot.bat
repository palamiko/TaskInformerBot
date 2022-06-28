
@set token="token"
@set login="login"
@set password="passwd"
@set count="4"

@python ./main.py -t %token% -l %login% -p %password%
pause