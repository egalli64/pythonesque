"""
Python Crash Course, Third Edition https://ehmatthes.github.io/pcc_3e/
My notes: https://github.com/egalli64/pythonesque/pcc3

Chapter 11 - Testing your code - A Class to Test
"""
import unittest
from e2_survey import AnonymousSurvey


class TestName(unittest.TestCase):
    def setUp(self):
        """A survey that will be available to all test functions."""
        self.language = AnonymousSurvey('What language did you first learn?')

    def test_store_single_response(self):
        """Test that a single response is stored properly."""
        self.language.store_response('English')
        self.assertIn('English', self.language.responses)

    def test_store_three_responses(self):
        """Test that three individual responses are stored properly."""
        responses = ['English', 'Spanish', 'Mandarin']
        for response in responses:
            self.language.store_response(response)

        for response in responses:
            self.assertIn(response, self.language.responses)


if __name__ == '__main__':
    unittest.main()
