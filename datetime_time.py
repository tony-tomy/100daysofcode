#!python3

import time
import calendar

ticks = time.time()

print("No of ticks since 12:00 am January 1st, 1970 : ",ticks )

print(time.localtime())

local_time = time.localtime(time.time())

print(local_time)

# convert time in readable format
print(time.asctime(local_time))

# calender related functions

calc = calendar.month(2020,2)

print(calc)

print(calendar.isleap(2020))

