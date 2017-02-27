"""
HackerRank Cracking the Coding Interview  Sorting: Comparator
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/02/hackerrank-sorting-comparator.html
      https://www.hackerrank.com/challenges/ctci-comparator-sorting
"""
import unittest
from functools import cmp_to_key
from operator import attrgetter
from hr.ctci_comparator_sorting import Player


class TestSolution(unittest.TestCase):

    def test_provided_1(self):
        data = {'amy': 100, 'david': 100, 'heraldo': 50, 'aakansha': 75, 'aleksa': 150}
        players = []
        for k, v in data.items():
            players.append(Player(k, v))

        players.sort(key=cmp_to_key(Player.comparator))

        self.assertEqual(5, len(players))
        self.assertEqual('aleksa', players[0].name)
        self.assertEqual('amy', players[1].name)
        self.assertEqual('david', players[2].name)
        self.assertEqual('aakansha', players[3].name)
        self.assertEqual('heraldo', players[4].name)

    def test_provided_attrgetter(self):
        data = {'amy': 100, 'david': 100, 'heraldo': 50, 'aakansha': 75, 'aleksa': 150}
        players = []
        for k, v in data.items():
            players.append(Player(k, v))

        players.sort(key=attrgetter('name'))
        players.sort(key=attrgetter('score'), reverse=True)

        self.assertEqual(5, len(players))
        self.assertEqual('aleksa', players[0].name)
        self.assertEqual('amy', players[1].name)
        self.assertEqual('david', players[2].name)
        self.assertEqual('aakansha', players[3].name)
        self.assertEqual('heraldo', players[4].name)

    def test_ex_aequo(self):
        players = []
        for i in range(3):
            players.append(Player('Tom' + chr(ord('k') - i), 100))

        players.sort(key=cmp_to_key(Player.comparator))

        self.assertEqual(3, len(players))
        self.assertEqual('Tomi', players[0].name)
        self.assertEqual('Tomj', players[1].name)
        self.assertEqual('Tomk', players[2].name)

    def test_ex_aequo_attrgetter(self):
        players = []
        for i in range(3):
            players.append(Player('Tom' + chr(ord('k') - i), 100))

        players.sort(key=attrgetter('name'))
        players.sort(key=attrgetter('score'), reverse=True)

        self.assertEqual(3, len(players))
        self.assertEqual('Tomi', players[0].name)
        self.assertEqual('Tomj', players[1].name)
        self.assertEqual('Tomk', players[2].name)


if __name__ == '__main__':
    unittest.main()
