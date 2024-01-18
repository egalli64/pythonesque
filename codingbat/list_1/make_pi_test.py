"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

List 1: https://codingbat.com/python/List-1
make_pi: https://codingbat.com/prob/p113659
"""
import unittest
from make_pi import make_pi


class TestMakePi(unittest.TestCase):
    def test_given(self):
        self.assertEqual(make_pi(), [3, 1, 4])


if __name__ == "__main__":
    unittest.main()
