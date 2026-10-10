"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque/cip

AI mock
"""


def call_gpt(request: str) -> str:
    """Mock a call to ChatGPT."""
    match len(request) % 3:
        case 0:
            return "Correct"
        case 1:
            return "Yes"
        case _:
            return "No"
