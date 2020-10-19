import unittest
from a2_add import add

class A2_AddTest(unittest.TestCase):
    def test_plain(self):
        self.assertEqual(add(4, 3), 7)

    def test_zero(self):
        self.assertEqual(add(0, 0), 0)

    def test_signed(self):
        self.assertEqual(add(4, -3), 1)

    def test_negative(self):
        self.assertEqual(add(-4, -3), -7)

if __name__ == "__main__":
    unittest.main()