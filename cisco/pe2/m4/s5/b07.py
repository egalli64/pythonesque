"""
Cisco Network Academy
Python Essentials 2: https://skillsforall.com/course/python-essentials-2
My notes: https://github.com/egalli64/pythonesque - cisco/pe2 folder

PE2 Module 4 - Miscellaneous
 Section 5 - The datetime module - working with time- and date-related functions
 7. Creating time objects
 8. The time module
 9. The ctime() function
10. The gmtime() and localtime() functions
11. The asctime() and mktime() functions
"""
import datetime
import time

t = datetime.time(14, 53, 20, 1)

print("Time:", t)
print("Hour:", t.hour)
print("Minute:", t.minute)
print("Second:", t.second)
print("Microsecond:", t.microsecond)


class Student:
    def take_nap(self, seconds):
        print("I'm very tired. I have to take a nap. See you later.")
        time.sleep(seconds)
        print("I slept well! I feel great!")


student = Student()
student.take_nap(1)

ts = 1572879180
print(f"Timestamp {ts} converted to human readable time:", time.ctime(ts))

gmt = time.gmtime(ts)
print("gmtime, UTC:", gmt)
print("localtime  :", time.localtime(ts))

print("GMT made readable by asctime:", time.asctime(gmt))
print("UNIX time from GMT          :", time.mktime(gmt))