"""
HackerRank Algorithms Warmup Time Conversion
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.hackerrank.com/challenges/time-conversion/problem

07:05:45PM -> 19:05:45
"""


def timeConversion(s):
    comps = s.split(':')
    pm = True if comps[2][2] == 'P' else False
    hh = int(comps[0])
    if hh == 12:
        if pm:
            hour = comps[0]
        else:
            hour = '00'
    elif pm:
        hour = str(12 + hh)
    else:
        hour = comps[0]
    return hour + s[2:8]

print(timeConversion('07:05:45PM'))
print(timeConversion('12:40:22AM'))
print(timeConversion('12:45:54PM'))
