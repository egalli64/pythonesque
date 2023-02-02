"""
CodeEval URI Comparison
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.codeeval.com/open_challenges/80/
"""
import unittest

from c080 import solution


class TestCodeEval(unittest.TestCase):

    def test_provided(self):
        self.assertEqual(True, solution('http://abc.com:80/~smith/home.html',
                                         'http://ABC.com/%7Esmith/home.html'))

    def test_minimal(self):
        self.assertEqual(True, solution('HTTP://cnn.com', 'http://cnn.com'))

    def test_many_escaped(self):
        self.assertEqual(True, solution('HTTP://ABC.com:8081//index)(!)}"%`>})!~`)\'{>.html',
                                         'http://ABC.COM:8081//index%29%28%21%29%7D%22%25%60%3E%7D%29%21%7E%60%29%27%7B%3E.html'))

if __name__ == '__main__':
    unittest.main()
