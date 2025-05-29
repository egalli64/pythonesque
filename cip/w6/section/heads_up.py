"""
Code in Place 2025 https://codeinplace.stanford.edu/cip5
My notes: https://github.com/egalli64/pythonesque/cip

Week 6: #3 Heads Up

Milestones:
1: Read the provided function that loads all of the words from the file cswords.txt into a list.
2: Then, show a randomly chosen word from the list
3: Repeat: wait for the user to hit enter, then show another word.
"""

import random

# Name of the file to read in!
FILE_NAME = "cip/w6/section/cswords.txt"


def get_words_from_file():
    """
    This function has been implemented for you. It opens a file,
    and stores all of the lines into a list of strings.
    It returns a list of all lines in the file.
    """
    lines = []
    with open(FILE_NAME) as f:
        for line in f:
            line = line.strip()
            if line != "":
                lines.append(line)

    print(lines)
    return lines


def main():
    # M1
    words = get_words_from_file()
    while True:
        word = random.choice(words)
        # M2 / M3
        input(word)


if __name__ == "__main__":
    main()
