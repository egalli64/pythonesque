"""
Cisco Network Academy
Python Essentials 2: https://skillsforall.com/course/python-essentials-2
My notes: https://github.com/egalli64/pythonesque - cisco/pe2 folder

PE2 Module 3 - Object-Oriented Programming
 Section 4 – OOP: Methods
 8. LAB Days of the week
 class Weeker
 ctor parameters: a string in Mon Tue Wed Thu Fri Sat Sun, or raise a WeekDayError 
 object printable
 methods add_days(n) and subtract_days(n)
"""


class WeekDayError(Exception):
    pass


class Weeker:
    _days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    def __init__(self, day):
        try:
            self._day = Weeker._days.index(day)
        except ValueError:
            raise WeekDayError

    def __str__(self):
        return Weeker._days[self._day]

    def add_days(self, n):
        self._day = (self._day + n) % 7

    def subtract_days(self, n):
        self._day = (self._day - n) % 7


try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")
