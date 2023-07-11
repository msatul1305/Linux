
import time
from datetime import datetime
from dateutil.utils import today
print(time.time()) # Current time in milliseconds since midnight, January 1, 1970, GMT (the Unix time).
print(datetime.now())
print(today())

from datetime import datetime

# Get current date and time
now = datetime.now()

# extract attributes
print("Year:", now.year)
print("Month:", now.month)
print("Day =", now.day)

print("Hour:", now.hour)
print("Minute:", now.minute)
print("Second:", now.second)
print("Microsecond:", now.microsecond)


from datetime import date

today = date.today()
print('Current Date:', today)


import time

# get current time
print('Current Time:', time.ctime(time.time()))

# Output Sat Jul 17 07:07:09 2021

import time

# get current local time
t = time.localtime(time.time())

print('Current Time:', t)
print('Year:', t.tm_year)
print('Month:', t.tm_mday)
print('Day:', t.tm_mday)

print('Minutes:', t.tm_min)
print('Hours:', t.tm_hour)
print('Seconds:', t.tm_sec)
