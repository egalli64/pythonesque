"""
HackerRank Algorithms Implementation Jumping on the Clouds: Revisited

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited/problem

Given
- a list of [0, 1] representing clouds [cumulus, thunderheads]
- k, the jump size.
Knowing that
- we start from 0
- the list has to be considered circular
- we have a start energy level of 100
- each jump costs 1
- each thundercloud touched costs an extra 2
- our task is getting back to origin
Return the final energy level
"""


def solution(clouds, jump):
    energy = 100

    energy -= len(clouds) // jump
    for i in range(0, len(clouds), jump):
        if clouds[i]:
            energy -= 2

    return energy

if __name__ == '__main__':
    _, k = map(int, input().split())
    items = list(map(int, input().split()))
    print(solution(items, k))