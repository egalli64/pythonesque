"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original code: https://github.com/fluentpython/example-code-2e/
My playground: https://github.com/egalli64/pythonesque/ fluent folder

Iterating on a Sentence
"""
from e01 import Sentence

# instantiate a Sentence
s = Sentence('"The time has come," the Walrus said,')

# using the Sentence representation
print(s)

# since Sentence is an Iterable (being a Sequence, having defined __getitem__), we could iterate on it
for word in s:
    print(word)

# Being iterable, a Sentence could be used to initialize a list
# still, the lack of __iter__ could confuse a linter and give a warning here
words = list(s)
print(words)

# Sentence is a Sequence, so it could be used as such:
print(s[0], s[5], s[-1])
