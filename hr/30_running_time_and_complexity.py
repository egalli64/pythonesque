"""
Hackerrank Tutorials  30 Days of Code  Day 25: Running Time and Complexity
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.hackerrank.com/challenges/30-running-time-and-complexity
"""


def is_prime(number):
    if number == 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False

    for i in range(3, number, 2):
        if i ** 2 > number:
            break
        if number % i == 0:
            return False
    return True

if __name__ == '__main__':
    size = int(input())
    for _ in range(size):
        n = int(input())
        print('Prime' if is_prime(n) else 'Not prime')
