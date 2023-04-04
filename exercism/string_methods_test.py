"""
Exercism Python track

Source: https://exercism.org/tracks/python
My solutions: https://github.com/egalli64/pythonesque/exercism

Little Sister's Essay https://exercism.org/tracks/python/exercises/little-sisters-essay

Functions to help edit essay homework using string manipulation.
"""
import unittest
from string_methods import *


class TestLittleSisterEssay(unittest.TestCase):
    def test_given_capitalize_title(self):
        title = 'my hobbies'
        expected_result = 'My Hobbies'
        self.assertEqual(capitalize_title(title), expected_result)

    def test_given_check_sentence_ending(self):
        self.assertTrue(check_sentence_ending(
            'I like to hike, bake, and read.'))

    def test_given_clean_up_spacing(self):
        sentence = ' I like to go on hikes with my dog.  '
        expected = 'I like to go on hikes with my dog.'
        self.assertEqual(clean_up_spacing(sentence), expected)

    def test_given_replace_word_choice(self):
        sentence = 'I bake good cakes.'
        old = 'good'
        new = 'amazing'
        expected = 'I bake amazing cakes.'
        self.assertEqual(replace_word_choice(sentence, old, new), expected)


if __name__ == '__main__':
    unittest.main()
