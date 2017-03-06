"""
CodeEval Email Validation
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.codeeval.com/open_challenges/35/
"""
import unittest
from ce.c035 import solution


class TestCodeEval(unittest.TestCase):

    def test_provided_1(self):
        self.assertEqual('true', solution('foo@bar.com'))

    def test_provided_2(self):
        self.assertEqual('false', solution('this is not an email id'))

    def test_provided_3(self):
        self.assertEqual('false', solution('admin#codeeval.com'))

    def test_provided_4(self):
        self.assertEqual('true', solution('good123@bad.com'))

    def test_bad_tail(self):
        self.assertEqual('false', solution('good123@bad.com!'))

    def test_dot(self):
        self.assertEqual('true', solution('tom.jones@example.com'))

    def test_dots(self):
        self.assertEqual('true', solution('hugo.de.vries@example.com'))

    def test_more_dots(self):
        self.assertEqual('true', solution('hugo.de.vries@my.example.com'))

    def test_quoted(self):
        self.assertEqual('true', solution('"h@x"@example.com'))

    def test_quoted_bad(self):
        self.assertEqual('false', solution('is"h@x"bad@example.com'))

    def test_plus(self):
        self.assertEqual('true', solution('h+42@example.com'))

if __name__ == '__main__':
    unittest.main()
