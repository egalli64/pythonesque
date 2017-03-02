"""
Plural Names Iterator
Based on Dive into Python 3
Chapter 7 Classes & Iterators, sections 6
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      http://www.diveintopython3.net/
"""
import re


def match_apply(pattern, search, replace):
    def match(word):
        return re.search(pattern, word)

    def apply(word):
        return re.sub(search, replace, word)

    return match, apply


class Rules:
    filename = 'plural_names_rules.txt'

    def __init__(self, filename=None):
        if filename:
            self.filename = filename

        self.rules = []
        with open(self.filename) as patterns:
            for line in patterns:
                pattern, search, replace = line.split()
                self.rules.append(match_apply(pattern, search, replace))

    def __iter__(self):
        self.index = -1
        return self

    def __next__(self):
        self.index += 1
        if len(self.rules) > self.index:
            return self.rules[self.index]
        raise StopIteration

rules = Rules()


def plural(noun):
    for match, apply in rules:
        if match(noun):
            return apply(noun)
    return '???'
