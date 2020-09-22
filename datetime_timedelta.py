#!python3

from datetime import datetime
from datetime import timedelta

t = timedelta(days= 4, hours= 10)

print(t.days)

print(t.seconds)

print(t.seconds/3600)

eta = timedelta(hours= 4)

today = datetime.today()

print(today)

print(today+eta)

print(str(today+eta))
