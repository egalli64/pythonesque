"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

Logic 1: https://codingbat.com/python/Logic-1
cigar_party: https://codingbat.com/prob/p195669
"""
import unittest
from cigar_party import cigar_party


class TestCigarParty(unittest.TestCase):
    def test_given_1(self):
        self.assertEqual(cigar_party(30, False), False)

    def test_given_2(self):
        self.assertEqual(cigar_party(50, False), True)

    def test_given_3(self):
        self.assertEqual(cigar_party(70, True), True)


if __name__ == "__main__":
    unittest.main()
