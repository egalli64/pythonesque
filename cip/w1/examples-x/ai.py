"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque/cip

AI mock
"""


def call_gpt(request: str) -> str:
    """Mock a call to ChatGPT"""
    if "apple" in request:
        return "manzana"
    elif "hello" in request:
        return "bonjour"
    else:
        return "unknown"
