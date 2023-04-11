"""
Exercism Python track

Source: https://exercism.org/tracks/python
My solutions: https://github.com/egalli64/pythonesque/exercism

Chaitana's Colossal Coaster https://exercism.org/tracks/python/exercises/chaitanas-colossal-coaster

Functions to manage and organize queues at Chaitana's roller coaster.
"""
import unittest
from list_methods import *


class TestChaitanaColossalCoaster(unittest.TestCase):
    def test_given_add_me_to_the_queue(self):
        express = ["Tony", "Bruce"]
        normal = ["RobotGuy", "WW"]

        tickets = [1, 0]
        persons = ["RichieRich", "HawkEye"]
        expected_results = [["Tony", "Bruce", "RichieRich"], [
            "RobotGuy", "WW", "HawkEye"]]

        for (ticket, person, expected) in zip(tickets, persons, expected_results):
            with self.subTest(input_data=person, output_data=expected):
                actual = add_me_to_the_queue(express, normal, ticket, person)
                self.assertEqual(actual, expected)

    def test_given_find_my_friend(self):
        queue = ["Natasha", "Steve", "T'challa", "Wanda", "Rocket"]
        name = "Steve"
        expected = 1

        actual = find_my_friend(queue, name)
        self.assertEqual(actual, expected)

    def test_given_add_me_with_my_friends(self):
        queue = ["Natasha", "Steve", "T'challa", "Wanda", "Rocket"]
        index = 1
        name = "Bucky"
        expected = ["Natasha", "Bucky", "Steve", "T'challa", "Wanda", "Rocket"]

        actual = add_me_with_my_friends(queue, index, name)
        self.assertEqual(actual, expected)

    def test_given_remove_the_mean_person(self):
        queue = ["Natasha", "Steve", "Eltran", "Wanda", "Rocket"]
        person = "Eltran"
        expected = ["Natasha", "Steve", "Wanda", "Rocket"]

        actual = remove_the_mean_person(queue, person)
        self.assertEqual(actual, expected)

    def test_given_how_many_namefellows(self):
        queue = ["Natasha", "Steve", "Eltran", "Natasha", "Rocket"]
        person = "Natasha"
        expected = 2

        actual = how_many_namefellows(queue, person)
        self.assertEqual(actual, expected)

    def test_given_remove_the_last_person(self):
        queue = ["Natasha", "Steve", "Eltran", "Natasha", "Rocket"]
        expected = "Rocket"

        actual = remove_the_last_person(queue)
        self.assertEqual(actual, expected)

    def test_given_sorted_names(self):
        queue = ["Natasha", "Steve", "Eltran", "Natasha", "Rocket"]
        expected = ['Eltran', 'Natasha', 'Natasha', 'Rocket', 'Steve']

        actual = sorted_names(queue)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
