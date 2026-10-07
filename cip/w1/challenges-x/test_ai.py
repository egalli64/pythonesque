"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque/cip

pytest for the AI mock
"""
from ai import call_gpt


class TestAI:
    """The call_gpt mock is just an echo in disguise"""

    def test_none(self):
        assert call_gpt(None) is None  # type: ignore[arg-type]

    def test_empty(self):
        assert call_gpt("") == ""

    def test_plain(self):
        assert call_gpt("42") == "42"
