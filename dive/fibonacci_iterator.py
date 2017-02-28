"""
Fibonacci Iterator
Based on Dive into Python 3
Chapter 7 Classes & Iterators, section 7.5
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/02/fibonacci-iterator.html
      http://www.diveintopython3.net/
"""
import unittest


class Fibonacci:
    def __init__(self, top):
        self.top = top

    def __iter__(self):
        self.a = 0
        self.b = 1
        return self

    def __next__(self):
        if self.a > self.top:
            raise StopIteration

        result = self.a
        self.a, self.b = self.b, self.a + self.b
        return result


def fibonacci(top):
    a, b = 0, 1
    while a < top:
        yield a
        a, b = b, a + b


class TestFibonacci(unittest.TestCase):
    def test_list_1000(self):
        fib1000 = list(Fibonacci(1000))
        self.assertEqual(17, len(fib1000))
        self.assertEqual(987, fib1000[-1])

    def test_multiple_12(self):
        for candidate in Fibonacci(1000):
            if candidate and candidate % 12 == 0:
                break
        else:
            self.fail('No fibonacci multiple of 12 found!')
        self.assertEqual(144, candidate)
