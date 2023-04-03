"""
Exercism Python track

Source: https://exercism.org/tracks/python
My solutions: https://github.com/egalli64/pythonesque/exercism

Meltdown Mitigation https://exercism.org/tracks/python/exercises/meltdown-mitigation

Functions to prevent a nuclear meltdown.
"""
import unittest
from conditionals import *


class TestConditionals(unittest.TestCase):
    def test_given_is_criticality_balanced(self):
        self.assertTrue(is_criticality_balanced(750, 600))

    def test_given_reactor_efficiency(self):
        self.assertEqual(reactor_efficiency(200, 50, 15000), 'orange')

    def test_fail_safe(self):
        self.assertEqual(fail_safe(temperature=1000, neutrons_produced_per_second=30, threshold=5000), 'DANGER')


if __name__ == '__main__':
    unittest.main()
