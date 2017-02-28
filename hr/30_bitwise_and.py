"""
HackerRank 30 Days of Code  Day 29: Bitwise AND
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.hackerrank.com/challenges/30-bitwise-and
"""
t = int(input().strip())
for _ in range(t):
    n, k = map(int, input().split())
    print(k-1 if (k | k - 1) <= n else k-2)
