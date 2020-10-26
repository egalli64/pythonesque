import unittest
from b4_max_pair_linear import max_pair


class A2_AddTest(unittest.TestCase):
    def test_given_1(self):
        self.assertEqual(max_pair([1, 2, 3]), 6)

    def test_given_2(self):
        a = [int(x) for x in "7 5 14 2 8 8 10 1 2 3".split()]
        self.assertEqual(max_pair(a), 140)

    def test_bad(self):
        self.assertRaises(AssertionError, lambda: max_pair([1]))


if __name__ == "__main__":
    unittest.main()
