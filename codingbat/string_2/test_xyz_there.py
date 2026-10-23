"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque codingbat folder

String 2: https://codingbat.com/python/String-2
xyz_there: https://codingbat.com/prob/p149391
"""
from xyz_there import xyz_there, xyz_there_walrus


class TestXyzThere:
    def test_given_1(self):
        assert xyz_there("abcxyz") is True

    def test_given_2(self):
        assert xyz_there("abc.xyz") is False

    def test_given_3(self):
        assert xyz_there("xyz.abc") is True

    def test_empty(self):
        assert xyz_there("") is False

    def test_good_the_second(self):
        assert xyz_there(".xyzxyz") is True

    def test_walrus_given_1(self):
        assert xyz_there_walrus("abcxyz") is True

    def test_walrus_given_2(self):
        assert xyz_there_walrus("abc.xyz") is False

    def test_walrus_given_3(self):
        assert xyz_there_walrus("xyz.abc") is True

    def test_walrus_empty(self):
        assert xyz_there_walrus("") is False

    def test_walrus_good_the_second(self):
        assert xyz_there_walrus(".xyzxyz") is True
