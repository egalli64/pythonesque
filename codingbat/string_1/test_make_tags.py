"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque codingbat folder

String 1: https://codingbat.com/python/String-1
make_tags: https://codingbat.com/prob/p132290
"""
from make_tags import make_tags, make_tags_f_str


class TestMakeTags:
    def test_given_1(self):
        assert make_tags("i", "Yay") == "<i>Yay</i>"

    def test_given_2(self):
        assert make_tags("i", "Hello") == "<i>Hello</i>"

    def test_given_3(self):
        assert make_tags("cite", "Yay") == "<cite>Yay</cite>"

    def test_given_f_str_1(self):
        assert make_tags_f_str("i", "Yay") == "<i>Yay</i>"

    def test_given_f_str_2(self):
        assert make_tags_f_str("i", "Hello") == "<i>Hello</i>"

    def test_given_f_str_3(self):
        assert make_tags_f_str("cite", "Yay") == "<cite>Yay</cite>"
