"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original code: https://github.com/fluentpython/example-code-2e/
My playground: https://github.com/egalli64/pythonesque/ fluent folder

Sentence refactored following the Iterator pattern
"""
import re
import reprlib

RE_WORD = re.compile(r'\w+')


class Sentence:
    """
    Sentence defines the iter dunder, so it is an iterable
    """

    def __init__(self, text):
        self.text: str = text
        self.words: list[str] = RE_WORD.findall(text)

    def __iter__(self):
        """Delegate the job, passing in the words on which to iterate"""
        return SentenceIterator(self.words)

    def __repr__(self):
        return f'Sentence({reprlib.repr(self.text)})'


class SentenceIterator:

    def __init__(self, words):
        """Work on the original list, keeping in index the next word to return"""
        self.words: list[str] = words
        self.index: int = 0

    def __next__(self):
        try:
            word = self.words[self.index]
            self.index += 1
            return word
        except IndexError:
            raise StopIteration()

    def __iter__(self):
        return self
