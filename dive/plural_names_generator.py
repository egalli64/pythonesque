"""
Plural Names Generator
Based on Dive into Python 3
Chapter 6 Closures & Generations, sections 6
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/03/plural-names-generator.html
      http://www.diveintopython3.net/
"""
import re


def match_apply(pattern, search, replace):
    def match(word):
        return re.search(pattern, word)

    def apply(word):
        return re.sub(search, replace, word)

    return match, apply


def rules(file):
    with open(file) as patterns:
        for line in patterns:
            pattern, search, replace = line.split()
            yield match_apply(pattern, search, replace)


def plural(noun, file='plural_names_rules.txt'):
    for match, apply in rules(file):
        if match(noun):
            return apply(noun)
    return '???'
