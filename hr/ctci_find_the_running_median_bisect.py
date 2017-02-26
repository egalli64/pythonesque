"""
Tutorials  Cracking the Coding Interview  Heaps: Find the Running Median (sort of cheating)
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/02/hackerrank-heaps-find-running-median.html
      https://www.hackerrank.com/challenges/ctci-find-the-running-median
"""
from bisect import insort

n = int(input().strip())
data = []

for i in range(n):
    item = int(input().strip())
    insort(data, item)
    pos = len(data) // 2
    result = float(data[pos])
    if len(data) % 2 == 0:
        result += data[pos - 1]
        result /= 2
    print(result)
