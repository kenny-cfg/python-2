import datetime

now = datetime.datetime.now()
print(now)

formatted_now = now.strftime('%a %d %b %H:%M:%S')
print(formatted_now)