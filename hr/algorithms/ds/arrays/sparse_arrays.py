"""
HackerRank  Data Structures  Arrays  Sparse Arrays
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.hackerrank.com/challenges/sparse-arrays/problem

given a bunch of strings w/repetitions
query the numerosity of some other strings
"""
from collections import defaultdict


if __name__ == '__main__':
    words = defaultdict(int)
    for _ in range(int(input())):
        words[input()] += 1

    for _ in range(int(input())):
        print(words[input()])
