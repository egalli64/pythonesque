"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque/cip

AI mock
"""
import random


def call_gpt(_: str) -> str:
    """Mock a call to ChatGPT, actually just return a random face."""
    return chr(random.randint(0x1F600, 0x1F64F))
