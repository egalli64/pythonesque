"""
Fibonacci Generator
Based on Dive into Python 3
Chapter 6 Closures & Generations, paragraph 6.6.1
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/02/fibonacci-generator.html
      http://www.diveintopython3.net/
"""
import unittest


def fibonacci(top):
    a, b = 0, 1
    while a < top:
        yield a
        a, b = b, a + b


class TestFibonacci(unittest.TestCase):
    def test_list_1000(self):
        fib1000 = list(fibonacci(1000))
        self.assertEqual(17, len(fib1000))
        self.assertEqual(987, fib1000[-1])

    def test_multiple_12(self):
        for candidate in fibonacci(1000):
            if candidate and candidate % 12 == 0:
                break
        else:
            self.fail('No fibonacci multiple of 12 found!')
        self.assertEqual(144, candidate)
