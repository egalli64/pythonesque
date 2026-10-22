"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque codingbat folder

Logic 1: https://codingbat.com/python/Logic-1
cigar_party: https://codingbat.com/prob/p195669
"""
from cigar_party import cigar_party


class TestCigarParty:
    """assuming pytest"""

    def test_given_1(self):
        assert cigar_party(30, False) is False

    def test_given_2(self):
        assert cigar_party(50, False) is True

    def test_given_3(self):
        assert cigar_party(70, True) is True
