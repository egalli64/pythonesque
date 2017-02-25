"""
Roman Numerals
Based on Dive into Python 3
Chapter 5 Regular Expressions, section 3
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/02/roman-numbers.html
"""
import unittest
import re


class TestPatterns(unittest.TestCase):

    def test_mils(self):
        pattern = '^M?M?M?$'
        for i in range(4):
            data = 'M' * i
            self.assertIsNotNone(re.search(pattern, data))
        self.assertIsNone(re.search(pattern, 'MMMM'))

    def test_full(self):
        pattern = '^M?M?M?(CM|CD|D?C?C?C?)(XC|XL|L?X?X?X?)(IX|IV|V?I?I?I?)$'
        for i in range(4):
            self.assertIsNotNone(re.search(pattern, 'C' * i))
        self.assertIsNone(re.search(pattern, 'CCCC'))
        self.assertIsNotNone(re.search(pattern, 'MMMCD'))
        self.assertIsNone(re.search(pattern, 'MCCD'))
        self.assertIsNotNone(re.search(pattern, 'MCMLXIV'))
        self.assertIsNone(re.search(pattern, 'IMM'))
        self.assertIsNotNone(re.search(pattern, 'MCMXCIX'))
        self.assertIsNotNone(re.search(pattern, 'MMXVII'))

    def test_full_count(self):
        pattern = '^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'
        for i in range(4):
            self.assertIsNotNone(re.search(pattern, 'C' * i))
        self.assertIsNone(re.search(pattern, 'CCCC'))
        self.assertIsNotNone(re.search(pattern, 'MMMCD'))
        self.assertIsNone(re.search(pattern, 'MCCD'))
        self.assertIsNotNone(re.search(pattern, 'MCMLXIV'))
        self.assertIsNone(re.search(pattern, 'IMM'))
        self.assertIsNotNone(re.search(pattern, 'MCMXCIX'))
        self.assertIsNotNone(re.search(pattern, 'MMXVII'))

if __name__ == '__main__':
    unittest.main()
