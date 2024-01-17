"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

String 1: https://codingbat.com/python/String-1
hello_name: https://codingbat.com/prob/p115413
"""
import unittest
from hello_name import hello_name, hello_name_f_str


class TestDiff21(unittest.TestCase):
    def test_given_1(self):
        self.assertEqual(hello_name("Bob"), "Hello Bob!")

    def test_given_2(self):
        self.assertEqual(hello_name("Alice"), "Hello Alice!")

    def test_given_3(self):
        self.assertEqual(hello_name("X"), "Hello X!")

    def test_given_f_str_1(self):
        self.assertEqual(hello_name_f_str("Bob"), "Hello Bob!")

    def test_given_f_str_2(self):
        self.assertEqual(hello_name_f_str("Alice"), "Hello Alice!")

    def test_given_f_str_3(self):
        self.assertEqual(hello_name_f_str("X"), "Hello X!")


if __name__ == "__main__":
    unittest.main()
