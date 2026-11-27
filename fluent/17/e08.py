"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original code: https://github.com/fluentpython/example-code-2e/
My playground: https://github.com/egalli64/pythonesque/ fluent folder

Sentence: refactored to be lazy
"""
import re
import reprlib

RE_WORD = re.compile(r'\w+')


class Sentence:
    """Get the current word on demand by generator"""

    def __init__(self, text):
        self.text = text

    def __iter__(self):
        # finditer returns an iterator on the matches
        for match in RE_WORD.finditer(self.text):
            # extract the actual matching text from the current match
            yield match.group()

    def __repr__(self):
        return f'Sentence({reprlib.repr(self.text)})'
