"""
edX UCSanDiegoX - Algorithmic Design and Techniques
https://www.edx.org/learn/algorithms/the-university-of-california-san-diego-algorithmic-design-and-techniques
My notes: https://github.com/egalli64/pythonesque folder algs200x/w3

Week 3 - greedy algorithms: Maximizing Your Salary
Given a list of strings in ['1' ... '999'] join them to a single number, as large as possible
"""


def filled(token: str) -> str:
    """Between 900 and 9, I should choose 9"""
    while len(token) < 3:
        token += token[-1]
    return token


def solution(tokens):
    tokens.sort(key=filled, reverse=True)

    return ''.join(tokens)
