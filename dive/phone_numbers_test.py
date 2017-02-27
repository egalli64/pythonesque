"""
Parsing Phone Numbers
Based on Dive into Python 3
Chapter 5 Regular Expressions, section 6
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/02/phone-numbers.html
"""
import unittest
import re


class TestPatterns(unittest.TestCase):
    def test_simple_number(self):
        pattern = re.compile(r'^(\d{3})-(\d{3})-(\d{4})$')
        result = pattern.search('800-555-1212')
        self.assertIsNotNone(result)

        groups = result.groups()
        self.assertEqual(3, len(groups))
        self.assertEqual('800', groups[0])
        self.assertEqual('555', groups[1])
        self.assertEqual('1212', groups[2])

    def test_simple_number_ext_fail(self):
        pattern = re.compile(r'^(\d{3})-(\d{3})-(\d{4})$')
        result = pattern.search('800-555-1212-123')
        self.assertIsNone(result)

    def test_number_plain(self):
        pattern = re.compile(r'(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$')
        result = pattern.search('800-555-1212')
        self.assertIsNotNone(result)

        groups = result.groups()
        self.assertEqual(4, len(groups))
        self.assertEqual('800', groups[0])
        self.assertEqual('555', groups[1])
        self.assertEqual('1212', groups[2])
        self.assertEqual('', groups[3])

    def test_number_ext(self):
        pattern = re.compile(r'(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$')
        result = pattern.search('800-555-1212-12')
        self.assertIsNotNone(result)

        groups = result.groups()
        self.assertEqual(4, len(groups))
        self.assertEqual('800', groups[0])
        self.assertEqual('555', groups[1])
        self.assertEqual('1212', groups[2])
        self.assertEqual('12', groups[3])

    def test_number_leading_blah(self):
        pattern = re.compile(r'(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$')
        result = pattern.search('The number is: 800-555-1212 ext. 12')
        self.assertIsNotNone(result)

        groups = result.groups()
        self.assertEqual(4, len(groups))
        self.assertEqual('800', groups[0])
        self.assertEqual('555', groups[1])
        self.assertEqual('1212', groups[2])
        self.assertEqual('12', groups[3])

    def test_number_compact(self):
        pattern = re.compile(r'(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$')
        result = pattern.search('800555121212')
        self.assertIsNotNone(result)

        groups = result.groups()
        self.assertEqual(4, len(groups))
        self.assertEqual('800', groups[0])
        self.assertEqual('555', groups[1])
        self.assertEqual('1212', groups[2])
        self.assertEqual('12', groups[3])

if __name__ == '__main__':
    unittest.main()
