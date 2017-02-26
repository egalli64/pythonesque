"""
Hackerrank Algorithms  Bit Manipulation  Changing Bits (sort of cheat)
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.hackerrank.com/challenges/changing-bits
"""


def set_bit(value, shift):
    return value | 1 << shift


def clear_bit(value, shift):
    return value & ~(1 << shift)

map_set = {'0': clear_bit, '1': set_bit}

if __name__ == '__main__':
    n, q = map(int, input().split())
    a = int(input(), 2)
    b = int(input(), 2)

    for _ in range(q):
        command, *params = input().split()
        if command == 'set_a':
            a = map_set[params[1]](a, int(params[0]))
        elif command == 'set_b':
            b = map_set[params[1]](b, int(params[0]))
        else:
            print(a+b >> int(params[0]) & 1, end='')
    print()
