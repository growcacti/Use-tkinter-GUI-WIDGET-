import datetime
now = datetime.datetime.today()
print(now.year)
print(now.month)
print(now.day)
myDate = now.date()
for i in range(1, 140, 14):
    print(myDate)
    myDate = myDate + datetime.timedelta(days=i)
