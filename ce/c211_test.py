"""
Chardonnay or Cabernet
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/01/codeeval-chardonnay-or-cabernet.html
      https://www.codeeval.com/open_challenges/211/
"""

import unittest
from c211 import solution


class TestChardonnay(unittest.TestCase):

    def test_provided_1(self):
        self.assertEqual('Merlot', solution('Cabernet Merlot Noir | ot'))

    def test_provided_2(self):
        self.assertEqual('Chardonnay Sauvignon', solution('Chardonnay Sauvignon | ann'))

    def test_provided_3(self):
        self.assertEqual('False', solution('Shiraz Grenache | o'))

    def test_reversed(self):
        self.assertEqual('pinot', solution('pinot | to'))


if __name__ == '__main__':
    unittest.main()
