"""
HackerRank Cracking the Coding Interview  Sorting: Comparator
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/02/hackerrank-sorting-comparator.html
      https://www.hackerrank.com/challenges/ctci-comparator-sorting
"""
from functools import cmp_to_key


class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        return '{} {}'.format(self.name, self.score)

    def comparator(self, rhs):
        if self.score == rhs.score:
            return 1 if self.name > rhs.name else -1
        return 1 if self.score < rhs.score else -1


if __name__ == '__main__':
    n = int(input())
    data = []
    for _ in range(n):
        name, score = input().split()
        score = int(score)
        player = Player(name, score)
        data.append(player)

    data = sorted(data, key=cmp_to_key(Player.comparator))
    for p in data:
        print(p)
