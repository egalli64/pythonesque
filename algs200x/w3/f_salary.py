"""
Maximizing Your Salary

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.edx.org/course/algorithmic-design-techniques-uc-san-diegox-algs200x
      week 3 - greedy algorithms
"""


def filler(token):
    while len(token) < 3:
        token += token[-1]
    return token


def solution(tokens):
    tokens.sort(key=filler, reverse=True)

    return ''.join(tokens)


if __name__ == '__main__':
    input()  # skip header
    data = list(input().split())

    print(solution(data))
