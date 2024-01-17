"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

String 1: https://codingbat.com/python/String-1
make_out_word: https://codingbat.com/prob/p129981
"""


def make_out_word(out, word):
    """
    Parameters:
        out str has length 4
        word str
    return the word inserted in the middle of out
    """
    return out[:2] + word + out[-2:]
