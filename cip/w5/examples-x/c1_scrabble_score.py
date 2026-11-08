"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque cip folder

Scrabble Score
"""
POINTS = {
    "a": 1, "e": 1, "i": 1, "l": 1, "n": 1, "o": 1, "r": 1, "s": 1, "t": 1, "u": 1,
    "d": 2, "g": 2,
    "b": 3, "c": 3, "m": 3, "p": 3,
    "f": 4, "h": 4, "v": 4, "w": 4, "y": 4,
    "k": 5,
    "j": 8, "x": 8,
    "q": 10, "z": 10,
}


def score(word):
    """
    Adds up the points for every letter in word.

    As designed: expect alphabetic letters only in word
    """
    result = 0
    for ch in word:
        result += POINTS[ch]
    return result


def main():
    while word := input("Enter a word: ").lower():
        print(f"{word} is worth {score(word)} points.")


if __name__ == "__main__":
    main()
