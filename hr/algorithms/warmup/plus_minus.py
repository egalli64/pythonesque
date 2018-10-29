"""
HackerRank Algorithms Warmup Plus Minus
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.hackerrank.com/challenges/plus-minus/problem
Given an array of integers,
 calculate the fractions of its elements that are positive, negative, and are zeros.
Print the decimal value of each fraction on a new line (six decimal places)
"""


def plusMinus(arr):
    positives = 0
    negatives = 0
    zeroes = 0

    for value in arr:
        if value > 0:
            positives += 1
        elif value < 0:
            negatives += 1
        else:
            zeroes += 1

    print('{:.6f}'.format(positives / len(arr)))
    print('{:.6f}'.format(negatives / len(arr)))
    print('{:.6f}'.format(zeroes / len(arr)))
