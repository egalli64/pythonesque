"""
CodeEval Prime Palindrome
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/02/codeeval-prime-palindrome.html
      https://www.codeeval.com/open_challenges/3/
"""
PRIMES = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31]


def is_prime(value):
    for prime in PRIMES:
        if prime**2 > value:
            break
        if value % prime == 0:
            return False

    return True

for candidate in range(989, 100, -2):
    if (candidate // 100 == candidate % 10) and is_prime(candidate):
        print(candidate)
        break
