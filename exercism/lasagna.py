"""
Exercism Python track

Source: https://exercism.org/tracks/python
My solutions: https://github.com/egalli64/pythonesque/exercism

Guido's Gorgeous Lasagna
https://exercism.org/tracks/python/exercises/guidos-gorgeous-lasagna/edit
"""

EXPECTED_BAKE_TIME = 40
TIME_FOR_LAYER = 2


def bake_time_remaining(elapsed: int):
    """
    Calculate the bake time remaining

    :param elapsed: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.
    """
    return EXPECTED_BAKE_TIME - elapsed


def preparation_time_in_minutes(layers: int):
    """
    Extra time required for extra layers

    :param layers: int - number of layers
    :return: int - extra time required
    """
    return layers * TIME_FOR_LAYER


def elapsed_time_in_minutes(layers: int, elapsed: int):
    """
    Total cooking time since the beginning

    :param layers: int - number of layers
    :param elapsed: int - baking time already elapsed.
    """
    return preparation_time_in_minutes(layers) + elapsed
