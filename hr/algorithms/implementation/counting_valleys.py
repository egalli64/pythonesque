"""
HackerRank Algorithms Implementation Counting Valleys

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.hackerrank.com/challenges/counting-valleys/problem

Given a string of {'U', 'D'}
representing representing steps Up and Down

Return the number of valleys (sequences below start-end level)
"""


def solution(trip):
    result = 0

    level = 0
    for c in trip:
        if c == 'U':
            level += 1
        else:
            level -= 1
            if level == -1:
                result += 1
    
    return result

if __name__ == '__main__':
    input()  # discard header
    print(solution(input().strip()))