"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

String 2: https://codingbat.com/python/String-2
end_other: https://codingbat.com/prob/p174314
"""
import unittest
from end_other import end_other


class TestEndOther(unittest.TestCase):
    def test_given_1(self):
        self.assertEqual(end_other("Hiabc", "abc"), True)

    def test_given_2(self):
        self.assertEqual(end_other("AbC", "HiaBc"), True)

    def test_given_3(self):
        self.assertEqual(end_other("abc", "abXabc"), True)


if __name__ == "__main__":
    unittest.main()
