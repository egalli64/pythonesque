"""
HackerRank 30 Days of Code Day 28: RegEx, Patterns, and Intro to Databases
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.hackerrank.com/challenges/30-regex-patterns
"""
import re
from bisect import insort

matching = []
n = int(input().strip())
for _ in range(n):
    name, email = input().split()
    if re.search('@gmail.com$', email):
        insort(matching, name)

print('\n'.join(matching))
