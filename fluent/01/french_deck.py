"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original file: https://github.com/fluentpython/example-code-2e/blob/master/01-data-model/frenchdeck.py
My playground: https://github.com/egalli64/pythonesque/ fluent folder

A Pythonic Card Deck
"""
import collections
from enum import StrEnum

# A Data Transfer Object to represent each single card
Card = collections.namedtuple('Card', ['rank', 'suit'])


class Suit(StrEnum):
    SPADES = 'spades'
    DIAMONDS = 'diamonds'
    CLUBS = 'clubs'
    HEARTS = 'hearts'


class Rank(StrEnum):
    TWO = '2'
    THREE = '3'
    FOUR = '4'
    FIVE = '5'
    SIX = '6'
    SEVEN = '7'
    EIGHT = '8'
    NINE = '9'
    TEN = '10'
    JACK = 'J'
    QUEEN = 'Q'
    KING = 'K'
    ACE = 'A'


class FrenchDeck:
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in Suit for rank in Rank]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]
