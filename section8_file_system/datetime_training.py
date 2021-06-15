import datetime
import time

now = datetime.datetime.now()
print(now)
print(now.isoformat())
print(now.strftime('%d/%m/%Y-%H:%M:%S'))

today = datetime.date.today()
print(today)
print(today.strftime('%d/%m/%y'))

t = datetime.time(hour=12, minute=29, second=0)
print(t)
print(t.isoformat())
print(t.strftime('%H_%M_%S'))

d = datetime.timedelta(weeks=1)
print(now - d)

print('-------')
time.sleep(1)
print('-------')
