"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original code: https://github.com/fluentpython/example-code-2e/
My playground: https://github.com/egalli64/pythonesque/ fluent folder

Sentence: refactored with generator
"""
import re
import reprlib

RE_WORD = re.compile(r'\w+')


class Sentence:
    """Simplify the iteration by generator"""

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __iter__(self):
        for word in self.words:
            yield word

    def __repr__(self):
        return f'Sentence({reprlib.repr(self.text)})'
