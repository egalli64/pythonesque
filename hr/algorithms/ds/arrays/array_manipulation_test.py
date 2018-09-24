"""
HackerRank  Data Structures  Arrays  Array Manipulation
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2018/09/hackerrank-array-manipulation.html
      https://www.hackerrank.com/challenges/crush/problem
"""
import unittest
from array_manipulation import NaiveManipulator, ArrayManipulator


class TestSolution(unittest.TestCase):
    def test_provided_naive_0(self):
        manipulator = NaiveManipulator(5)
        manipulator.set(1, 2, 100)
        manipulator.set(2, 5, 100)
        manipulator.set(3, 4, 100)
        self.assertEqual(200, manipulator.solution())

    def test_provided_naive_1(self):
        manipulator = NaiveManipulator(10)
        manipulator.set(1, 5, 3)
        manipulator.set(4, 8, 7)
        manipulator.set(6, 9, 1)
        self.assertEqual(10, manipulator.solution())

    def test_provided_naive_2(self):
        manipulator = NaiveManipulator(10)
        manipulator.set(2, 6, 8)
        manipulator.set(3, 5, 7)
        manipulator.set(1, 8, 1)
        manipulator.set(5, 9, 15)
        self.assertEqual(31, manipulator.solution())

    def test_naive(self):
        manipulator = NaiveManipulator(1_000)
        for _ in range(2_000):
            manipulator.set(10, 800, 1)
        self.assertEqual(2_000, manipulator.solution())


    def test_smarter(self):
        manipulator = ArrayManipulator(1_000)
        for _ in range(2_000):
            manipulator.set(10, 800, 1)
        self.assertEqual(2_000, manipulator.solution())

    def test_provided_0(self):
        manipulator = ArrayManipulator(5)
        manipulator.set(1, 2, 100)
        manipulator.set(2, 5, 100)
        manipulator.set(3, 4, 100)
        self.assertEqual(200, manipulator.solution())

    def test_provided_1(self):
        manipulator = ArrayManipulator(10)
        manipulator.set(1, 5, 3)
        manipulator.set(4, 8, 7)
        manipulator.set(6, 9, 1)
        self.assertEqual(10, manipulator.solution())

    def test_provided_2(self):
        manipulator = ArrayManipulator(10)
        manipulator.set(2, 6, 8)
        manipulator.set(3, 5, 7)
        manipulator.set(1, 8, 1)
        manipulator.set(5, 9, 15)
        self.assertEqual(31, manipulator.solution())


if __name__ == '__main__':
    unittest.main()
