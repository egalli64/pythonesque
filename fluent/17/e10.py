"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original code: https://github.com/fluentpython/example-code-2e/
My playground: https://github.com/egalli64/pythonesque/ fluent folder

Sentence: refactored by generator expression
"""
import re
import reprlib

RE_WORD = re.compile(r'\w+')


class Sentence:
    """Get the current word on demand by generator"""

    def __init__(self, text):
        self.text = text

    def __iter__(self):
        """Return a generator lazily based on the iterator on the regex"""
        return (match.group() for match in RE_WORD.finditer(self.text))

    def __repr__(self):
        return f'Sentence({reprlib.repr(self.text)})'
