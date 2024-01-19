"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

Logic 1: https://codingbat.com/python/Logic-1
squirrel_play: https://codingbat.com/prob/p135815
"""
import unittest
from squirrel_play import squirrel_play


class TestSquirrelPlay(unittest.TestCase):
    def test_given_1(self):
        self.assertEqual(squirrel_play(70, False), True)

    def test_given_2(self):
        self.assertEqual(squirrel_play(95, False), False)

    def test_given_3(self):
        self.assertEqual(squirrel_play(95, True), True)


if __name__ == "__main__":
    unittest.main()
