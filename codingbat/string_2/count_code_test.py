"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

String 2: https://codingbat.com/python/String-2
count_code: https://codingbat.com/prob/p186048
"""
import unittest
from count_code import count_code, count_code_walrus


class TestCountCode(unittest.TestCase):
    def test_given_1(self):
        self.assertEqual(count_code("aaacodebbb"), 1)

    def test_given_2(self):
        self.assertEqual(count_code("codexxcode"), 2)

    def test_given_3(self):
        self.assertEqual(count_code("cozexxcope"), 2)

    def test_given_walrus_1(self):
        self.assertEqual(count_code_walrus("aaacodebbb"), 1)

    def test_given_walrus_2(self):
        self.assertEqual(count_code("codexxcode"), 2)

    def test_given_walrus_3(self):
        self.assertEqual(count_code("cozexxcope"), 2)


if __name__ == "__main__":
    unittest.main()
