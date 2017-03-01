"""
Plural Names Generator
Based on Dive into Python 3
Chapter 6 Closures & Generations, sections 2, 3, 4
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/03/plural-names-generator.html
      http://www.diveintopython3.net/
"""
import unittest
from dive.plural_names_generator import plural


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
