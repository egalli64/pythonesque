"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque codingbat folder

String 2: https://codingbat.com/python/String-2
count_code: https://codingbat.com/prob/p186048
"""
from count_code import count_code, count_code_walrus


class TestCountCode:
    def test_given_1(self):
        assert count_code("aaacodebbb") == 1

    def test_given_2(self):
        assert count_code("codexxcode") == 2

    def test_given_3(self):
        assert count_code("cozexxcope") == 2

    def test_given_walrus_1(self):
        assert count_code_walrus("aaacodebbb") == 1

    def test_given_walrus_2(self):
        assert count_code("codexxcode") == 2

    def test_given_walrus_3(self):
        assert count_code("cozexxcope") == 2
