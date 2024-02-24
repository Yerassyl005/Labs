import datetime

today = datetime.date.today()
yesterday = datetime.date.today() - datetime.timedelta(days = 1)
tomorrow = datetime.date.today() + datetime.timedelta(days = 1)
print(yesterday, today, tomorrow)