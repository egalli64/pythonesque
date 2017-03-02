"""
Plural Names Iterator
Based on Dive into Python 3
Chapter 7 Classes & Iterators, sections 6
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      http://www.diveintopython3.net/
"""
import unittest
from dive.plural_names_iterator import plural


class TestPluralNames(unittest.TestCase):
    def test_box(self):
        self.assertEqual('boxes', plural('box'))

    def test_bush(self):
        self.assertEqual('bushes', plural('bush'))

    def test_soliloquy(self):
        self.assertEqual('soliloquies', plural('soliloquy'))

    def test_boy(self):
        self.assertEqual('boys', plural('boy'))

    def test_vacancy(self):
        self.assertEqual('vacancies', plural('vacancy'))

if __name__ == '__main__':
    unittest.main()
