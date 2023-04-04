"""
Exercism Python track

Source: https://exercism.org/tracks/python
My solutions: https://github.com/egalli64/pythonesque/exercism

Little Sister's Vocabulary https://exercism.org/tracks/python/exercises/little-sisters-vocab
"""
import unittest
from strings import *


class TestLittleSisterVocabulary(unittest.TestCase):
    def test_given_add_prefix_un(self):
        words = ['happy', 'manageable']
        expected_results = ['unhappy', 'unmanageable']
        for i, (word, expected) in enumerate(zip(words, expected_results)):
            with self.subTest(i, input_data=word, output_data=expected):
                self.assertEqual(add_prefix_un(word), expected)

    def test_given_make_word_groups(self):
        words = ['en', 'close', 'joy', 'lighten']
        expected_results = 'en :: enclose :: enjoy :: enlighten'
        self.assertEqual(make_word_groups(words), expected_results)

    def test_given_remove_suffix_ness(self):
        words = ['heaviness', 'sadness']
        expected_results = ['heavy', 'sad']
        for i, (word, expected) in enumerate(zip(words, expected_results)):
            with self.subTest(i, input_data=word, output_data=expected):
                self.assertEqual(remove_suffix_ness(word), expected)

    def test_given_adjective_to_verb(self):
        given_inputs = [('I need to make that bright.', -1), ('It got dark as the sun set.', 2)]
        expected_results = ['brighten', 'darken']
        for i, (args, expected) in enumerate(zip(given_inputs, expected_results)):
            with self.subTest(i, input_data=args, output_data=expected):
                self.assertEqual(adjective_to_verb(args[0], args[1]), expected)


if __name__ == '__main__':
    unittest.main()
