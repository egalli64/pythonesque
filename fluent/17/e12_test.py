"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original code: https://github.com/fluentpython/example-code-2e/
My playground: https://github.com/egalli64/pythonesque/ fluent folder
"""
from decimal import Decimal
from fractions import Fraction

from e12 import ArithmeticProgression


class TestArithmeticProgression:
    def test_int(self):
        actual = list(ArithmeticProgression(0, 1, 3))
        expected = [0, 1, 2]
        assert actual == expected

    def test_float(self):
        actual = list(ArithmeticProgression(1, .5, 3))
        expected = [1.0, 1.5, 2.0, 2.5]
        assert actual == expected

    def test_float_2(self):
        actual = list(ArithmeticProgression(0, 1 / 3, 1))
        expected = [0, 1 / 3, 2 / 3]
        assert actual == expected

    def test_fraction(self):
        actual = list(ArithmeticProgression(0, Fraction(1, 3), 1))
        expected = [0, Fraction(1, 3), Fraction(2, 3)]
        assert actual == expected

    def test_decimal(self):
        actual = list(ArithmeticProgression(0, Decimal('.1'), .3))
        expected = [Decimal('0'), Decimal('.1'), Decimal('.2')]
        assert actual == expected
