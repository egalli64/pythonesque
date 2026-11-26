"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original code: https://github.com/fluentpython/example-code-2e/
My playground: https://github.com/egalli64/pythonesque/ fluent folder

A Sentence as a sequence of words
"""
import re
import reprlib

RE_WORD = re.compile(r'\w+')


class Sentence:
    """
    A Sentence implements the sequence protocol, so it is an iterable
    """

    def __init__(self, text: str) -> None:
        self.text: str = text
        self.words: list[str] = RE_WORD.findall(text)

    def __getitem__(self, index: int) -> str:
        return self.words[index]

    def __len__(self) -> int:
        return len(self.words)

    def __repr__(self) -> str:
        return f'Sentence({reprlib.repr(self.text)})'
