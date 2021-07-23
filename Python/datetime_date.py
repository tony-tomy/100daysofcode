#!python3

from datetime import datetime
from datetime import date

datetime.today()

today = datetime.today()

print(type(today))

todaydate = date.today()

print(todaydate)

print(type(todaydate))

todaydate.month

todaydate.year

todaydate.day

christmas = date(2020, 12, 25)

christmas

if christmas is not todaydate:
    print("There are still "+ str((christmas-todaydate).days) + " days untill christmas")
else:
    print("Today is christmas")