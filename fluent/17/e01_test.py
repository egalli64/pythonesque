"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original code: https://github.com/fluentpython/example-code-2e/
My playground: https://github.com/egalli64/pythonesque/ fluent folder

A Sentence as a sequence of words
"""
from e01 import Sentence


class TestSentence:
    def test_plain(self):
        s = Sentence('To be, or not to be, that is the question')

        # the length of a sentence is the number of the words in it
        assert len(s) == 10
        assert s[1] == 'be'
        assert s[5] == 'be'

        # a sentence has its own peculiar representation
        assert repr(s) == "Sentence('To be, or no... the question')"
