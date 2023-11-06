"""
Cisco Network Academy
Python Essentials 2: https://skillsforall.com/course/python-essentials-2
My notes: https://github.com/egalli64/pythonesque - cisco/pe2 folder

PE2 Module 4 - Miscellaneous
 Section 6 - The calendar module - working with calendar-related functions
13. LAB The calendar module
    Derive MyCalendar from Calendar
    create count_weekday_in_year():
        take a year and a weekday as parameters
        return the number of occurrences of a specific weekday in the year
    ex:
        year=2019, weekday=0 gives 52
        year=2000, weekday=6 gives 53
"""
import calendar


class MyCalendar(calendar.Calendar):
    def count_weekday_in_year(self, year, weekday):
        result = 0
        for month in range(1, 13):
            for data in self.monthdays2calendar(year, month):
                if data[weekday][0] != 0:
                    result += 1
        return result


my_calendar = MyCalendar()
print(my_calendar.count_weekday_in_year(2019, calendar.MONDAY))
print(my_calendar.count_weekday_in_year(2000, calendar.SATURDAY))
