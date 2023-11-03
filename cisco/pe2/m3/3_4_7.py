"""
Cisco Network Academy
Python Essentials 2: https://skillsforall.com/course/python-essentials-2
My notes: https://github.com/egalli64/pythonesque - cisco/pe2 folder

PE2 Module 3 - Object-Oriented Programming
 Section 4 – OOP: Methods
 7. LAB The Timer class
 ctor parameters: hours [0..23], minutes [0..59], and seconds [0..59], defaulted to 0, 0, 0
 object printable in format "hh:mm:ss"
 methods next_second() and previous_second()
"""


def format(value):
    s = str(value)
    return '0' + s if value < 10 else s


class Timer:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self._hours = hours
        self._minutes = minutes
        self._seconds = seconds

    def __str__(self):
        return format(self._hours) + ":" + format(self._minutes) + ":" + format(self._seconds)

    def next_second(self):
        self._seconds += 1
        if self._seconds > 59:
            self._seconds = 0
            self._minutes += 1
            if self._minutes > 59:
                self._minutes = 0
                self._hours += 1
                if self._hours > 23:
                    self._hours = 0

    def prev_second(self):
        self._seconds -= 1
        if self._seconds < 0:
            self._seconds = 59
            self._minutes -= 1
            if self._minutes < 0:
                self._minutes = 59
                self._hours -= 1
                if self._hours < 0:
                    self._hours = 23


timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
