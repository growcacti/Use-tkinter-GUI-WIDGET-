import datetime

dates = []

now = datetime.datetime.today()


for i in range(1, 150):
     day = now.day + i

     date = now.strftime('%Y-%m-' + str(day))

     dates.append(date)

     print(date)
