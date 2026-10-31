"""
Coder-byte Challenges

Source: https://coderbyte.com/challenges
My solutions: https://github.com/egalli64/pythonesque coderbyte folder

Code-land Username Validation
"""
from codeland_username_validation import username_validation, re_username_validation


class TestUsernameValidation:
    def test_given_1(self):
        assert username_validation("aa_") == "false"

    def test_given_2(self):
        assert username_validation("u__hello_world123") == "true"

class TestReUsernameValidation:
    def test_given_1(self):
        assert re_username_validation("aa_") == "false"

    def test_given_2(self):
        assert re_username_validation("u__hello_world123") == "true"
