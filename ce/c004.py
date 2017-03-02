"""
CodeEval Sum of Primes
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/02/codeeval-sum-of-primes.html
      https://www.codeeval.com/open_challenges/4/
"""
from itertools import count

primes = [2, 3]


def is_prime(value):
    for prime in primes:
        if prime ** 2 > value:
            break
        elif i % prime == 0:
            return False
    return True

while len(primes) < 1000:
    for i in count(primes[-1] + 2, 2):
        if is_prime(i):
            primes.append(i)
            break

print(sum(primes))
