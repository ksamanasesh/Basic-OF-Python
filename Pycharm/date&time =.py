from datetime import datetime,timedelta,timezone,UTC,date,time

a = datetime.now()
print(a)
b = datetime.date(a)
print("Today is date :",b)
c = datetime.time(a)
print("Current time :",c)

