"""
HackerRank Tutorials  Cracking the Coding Interview  Stacks: Balanced Brackets
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/02/hackerrank-stacks-balanced-brackets.html
      https://www.hackerrank.com/challenges/ctci-balanced-brackets
"""


def solution(data):
    matches = {'(': ')', '[': ']', '{': '}'}

    stack = []
    for c in data:
        if c in matches.keys():
            stack.append(c)
        elif not stack or c != matches[stack.pop()]:
            return False
    return True if not stack else False

if __name__ == '__main__':
    line = input()

    print(solution(line))
