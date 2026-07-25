"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original file: https://github.com/fluentpython/example-code-2e/blob/master/01-data-model/frenchdeck.doctest
My playground: https://github.com/egalli64/pythonesque/ fluent folder

A Pythonic Card Deck
"""
from random import choice

from french_deck import Card, FrenchDeck

beer_card = Card('7', 'diamonds')
print(beer_card)

deck = FrenchDeck()

print(f"There are {len(deck)} cards in the deck.")
print(f"The first card is {deck[0].rank} of {deck[0].suit}.")
print(f"The last card is {deck[-1].rank} of {deck[-1].suit}.")
print("The first three cards in the deck are:")
for card in deck[:3]:
    print(card.rank, card.suit)

print("The cards in the last rank are:")
for card in deck[12::13]:
    print(card.rank, card.suit)

print("Check if Q hearts is in the deck:", Card('Q', 'hearts') in deck)
print("Check if Z hearts is in the deck:", Card('Z', 'hearts') in deck)

print("A randomly chosen card:", choice(deck))
