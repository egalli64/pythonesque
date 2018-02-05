"""
HackerRank Tutorials  Cracking the Coding Interview  Recursion: Fibonacci Numbers
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.hackerrank.com/challenges/ctci-fibonacci-numbers

Since the problem has the constraint that n should be in (0 .. 30]
 there's no need of anything fancy in the code.
"""


def fibonacci(n):
    if n == 0:
        return 0;
    if n < 3:
        return 1;
    return fibonacci(n-1) + fibonacci(n-2)


if __name__ == '__main__':
    n = int(input())

    print(fibonacci(n))
