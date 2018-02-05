"""
HackerRank Tutorials  Cracking the Coding Interview  Hash Tables: Ransom Note
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/02/hackerrank-hash-tables-ransom-note.html
      https://www.hackerrank.com/challenges/ctci-ransom-note
"""
from collections import Counter


def solution(magazine, ransom):
    available = Counter(magazine)
    needed = Counter(ransom)

    for word in needed:
        if needed.get(word) > available.get(word, 0):
            return False
    return True


if __name__ == '__main__':
    input()
    magazine = input().strip().split(' ')
    ransom = input().strip().split(' ')
    print("Yes") if solution(magazine, ransom) else print("No")
