"""
Cisco Network Academy
Python Essentials 2: https://skillsforall.com/course/python-essentials-2
My notes: https://github.com/egalli64/pythonesque - cisco/pe2 folder

PE2 Module 4 - Miscellaneous
 Section 5 - The datetime module - working with time- and date-related functions
12. Creating datetime objects
15. Date and time formatting
16. The strftime() function in the time module
17. The strptime() method
18. Date and time operations
19. Creating timedelta objects
"""
from datetime import datetime, date, timedelta
import time

print("today :", datetime.today())
print("now   :", datetime.now())
print("utcnow:", datetime.utcnow())

dt = datetime(2020, 10, 4, 14, 55)
print("Timestamp:", dt.timestamp())

d = date(2020, 1, 4)
print(d.strftime("%Y/%m/%d"))
print(dt.strftime("%y/%B/%d %H:%M:%S"))

timestamp = 1572879180
st = time.gmtime(timestamp)

print(time.strftime("%Y/%m/%d %H:%M:%S", st))
print(time.strftime("%Y/%m/%d %H:%M:%S"))

print(datetime.strptime("2019/11/04 14:53:00", "%Y/%m/%d %H:%M:%S"))
print(time.strptime("2019/11/04 14:53:00", "%Y/%m/%d %H:%M:%S"))

# timedelta
d1 = date(2020, 11, 4)
d2 = date(2019, 11, 4)
print(d1 - d2)

dt1 = datetime(2020, 11, 4, 0, 0, 0)
dt2 = datetime(2019, 11, 4, 14, 53, 0)
print(dt1 - dt2)

delta = timedelta(weeks=2, days=2, hours=3)
print("A time delta:", delta)
print("Days        :", delta.days)
print("Seconds     :", delta.seconds)
print("Microseconds:", delta.microseconds)

delta2 = delta * 2
print("Double delta:", delta2)

d = date(2019, 10, 4) + delta2
print(d)

dt = datetime(2019, 10, 4, 14, 53) + delta2
print(dt)
