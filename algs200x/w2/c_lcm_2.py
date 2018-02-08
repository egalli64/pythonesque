# Smarter Least Common Multiple calculator
from math import gcd


def lcm(a, b):
    return (a * b) // gcd(a, b)


if __name__ == '__main__':
    lhs, rhs = map(int, input().split())
    print(lcm(lhs, rhs))
