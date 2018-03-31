"""
HackerRank Algorithms Implementation Day of the Programmer

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.hackerrank.com/challenges/day-of-the-programmer/problem

Given an year in [1700, 2700], return the 256th day in Russia for that year.
In 1918 they moved from Julian to Gregorian calendar.
"""

def solution(year):
    if (year == 1918):
        return '26.09.1918'
    elif ((year <= 1917) and (year%4 == 0)) or ((year%400 == 0) or ((year%4 ==0) and (year%100))):
        return '12.09.' + str(year)

    return '13.09.'  + str(year)

if __name__ == '__main__':
    print(solution(int(input())))
