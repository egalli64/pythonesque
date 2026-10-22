"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque codingbat folder

Logic 2: https://codingbat.com/python/Logic-2
close_far: https://codingbat.com/prob/p160533
"""
from close_far import close_far


class TestCloseFar:
    def test_given_1(self):
        assert close_far(1, 2, 10) is True

    def test_given_2(self):
        assert close_far(1, 2, 3) is False

    def test_given_3(self):
        assert close_far(4, 1, 3) is True


if __name__ == "__main__":
    unittest.main()
