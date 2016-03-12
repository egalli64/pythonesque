"""
Based on Week 2 > Lecture 4 - Stochastic Programming and Statistical Thinking - L4 Problem 3
From edx.org - MITx: 6.00.2x Introduction to Computational Thinking and Data Science
Original function signature: stdDevOfLengths(L)

More info: http://pythonesque.blogspot.com/2016/03/strings-standard-deviation.html
"""

import unittest
import math


def standard_deviation(strings):
    """
    :param strings: a list of strings
    :returns the standard deviation of the lengths of the strings, or NaN.
    :rtype float
    """

    if not strings:
        return float('NaN')

    lengths = [len(s) for s in strings]
    mean = math.fsum(lengths) / len(lengths)

    sq_sum = 0.0
    for l in lengths:
        sq_sum += (l - mean) ** 2

    return math.sqrt(sq_sum / len(lengths))


class StdDevTest(unittest.TestCase):
    def test_none(self):
        self.assertTrue(math.isnan(standard_deviation(None)))

    def test_empty(self):
        strings = []
        self.assertTrue(math.isnan(standard_deviation(strings)))

    def test_1(self):
        strings = ['a', 'z', 'p']
        self.assertEqual(standard_deviation(strings), 0)

    def test_2(self):
        strings = ['apples', 'oranges', 'kiwis', 'pineapples']
        self.assertAlmostEqual(standard_deviation(strings), 1.8708, delta=0.0001)

    def test_3(self):
        strings = ['mftbycwac', 'rhqbqawnfl', 'clgzh', 'ilqy', 'ckizvsgpnhlx', 'kziugguuzvqarw', 'xqewrmvu', 'ktojfqkailswnb']
        self.assertEqual(standard_deviation(strings), 3.5355339059327378)

    def test_4(self):
        strings = ['zgbljwombl', 'slkpmjqmjaaw', 'nddl', 'irlzne', '', 'poieczhxoqom', 'waqyiipysskxk', 'dloxspi', 'sk']
        self.assertEqual(standard_deviation(strings), 4.447221354708778)

    def test_bad_data(self):
        with self.assertRaises(TypeError):
            standard_deviation([1, 2, 3])

if __name__ == '__main__':
    unittest.main()