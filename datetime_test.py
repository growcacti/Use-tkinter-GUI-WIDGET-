import datetime


now = datetime.datetime.today()
long_ago = datetime.datetime(1999, 3, 14, 12, 30, 58)
print(now.strftime("%Y,%B,%d,%a"))
print(now.strftime("%a, %d %B %Y"))
print(long_ago) # remember that this calls str automatically
print(long_ago < now)
difference = now - long_ago
print(type(difference))
print(difference)
# below print the next 10 dates two weeks apart starting from today
now = datetime.datetime.today()
print(now.year)
print(now.month)
print(now.day)
myDate = now.date()
for i in range(0, 140, 14):
##    print(myDate)
    myDate2 = myDate + datetime.timedelta(days=i)
    print(myDate2)
    p = 365/2
    print(p)
for i in range(0, 183,182):
    me3 = myDate + datetime.timedelta(days=i)
    print(me3.strftime("%a, %d %B %Y"))
