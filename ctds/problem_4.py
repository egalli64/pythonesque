"""
Based on Week 2 > Lecture 4 - Stochastic Programming and Statistical Thinking - L4 Problem 4, point 4
From edx.org - MITx: 6.00.2x Introduction to Computational Thinking and Data Science

More info: http://pythonesque.blogspot.com
"""

import math
import numpy
import unittest


def cv(data):
    """
    :param data a list of numbers
    :returns its coefficient of variation, or NaN.
    :rtype float
    """
    if not data:
        return float('NaN')

    mean = sum(data) / float(len(data))
    if mean == 0:
        return float('NaN')

    sq_sum = 0.0
    for d in data:
        sq_sum += (d - mean) ** 2
    stddev = math.sqrt(sq_sum / len(data))

    return stddev / mean


def cv_(data):
    """
    :param data a list of numbers
    :returns its coefficient of variation, or NaN.
    :rtype float
    """
    if not data:
        return float('NaN')

    mean = numpy.mean(data)
    if mean == 0.0:
        return float('NaN')

    return numpy.std(data) / mean


class CV(unittest.TestCase):
    def test_none(self):
        coll = None
        self.assertTrue(math.isnan(cv(coll)))
        self.assertTrue(math.isnan(cv_(coll)))

    def test_empty(self):
        self.assertTrue(math.isnan(cv([])))
        self.assertTrue(math.isnan(cv_([])))

    def test_zero_mean(self):
        coll = [1, 2, 0, -1, -2]
        self.assertTrue(math.isnan(cv(coll)))
        self.assertTrue(math.isnan(cv_(coll)))

    def test_std_var_0(self):
        coll = [42, 42, 42]
        self.assertEqual(cv(coll), 0)
        self.assertEqual(cv_(coll), 0)

    def test_1(self):
        coll = [0, 0, 6, 6]
        self.assertEqual(cv(coll), 1)
        self.assertEqual(cv_(coll), 1)

    def test_dot5(self):
        coll = [10, 4, 12, 15, 20, 5]
        self.assertAlmostEqual(cv(coll), 0.503, delta=0.001)
        self.assertAlmostEqual(cv_(coll), 0.503, delta=0.001)

if __name__ == '__main__':
    unittest.main()