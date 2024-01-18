"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

Logic 1: https://codingbat.com/python/Logic-1
cigar_party: https://codingbat.com/prob/p195669
"""


def cigar_party(cigars, is_weekend):
    """
    Parameters:
        cigars int
        is_weekend bool
    return True if cigars in [40, 60] in not weekend, for weekend cigars should just be 40+
    """
    if cigars < 40:
        return False
    else:
        return cigars <= 60 if not is_weekend else True
