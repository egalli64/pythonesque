"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

String 2: https://codingbat.com/python/String-2
cat_dog: https://codingbat.com/prob/p164876
"""
import unittest
from cat_dog import cat_dog


class TestDoubleChar(unittest.TestCase):
    def test_given_1(self):
        self.assertEqual(cat_dog("catdog"), True)

    def test_given_2(self):
        self.assertEqual(cat_dog("catcat"), False)

    def test_given_3(self):
        self.assertEqual(cat_dog("1cat1cadodog"), True)


if __name__ == "__main__":
    unittest.main()
