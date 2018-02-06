"""
HackerRank Tutorials  Cracking the Coding Interview  Strings: Making Anagrams
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/02/hackerrank-strings-making-anagrams.html
      https://www.hackerrank.com/challenges/ctci-making-anagrams
"""
from collections import Counter


def solution(a, b):
    counter = Counter(a)

    extra = 0
    for ch in b:
        if counter.get(ch):
            counter[ch] -= 1
        else:
            extra += 1

    return sum(counter.values()) + extra


if __name__ == '__main__':
    a = input().strip()
    b = input().strip()

    print(solution(a, b))
