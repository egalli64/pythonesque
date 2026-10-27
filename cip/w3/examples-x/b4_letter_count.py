"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque cip folder

Letter Count
"""


def main():
    word = input("Enter a word: ")
    letter = input("Enter a letter: ")

    count = 0
    for x in word:
        if x == letter:
            count += 1

    print(f"{letter} appears {count} times in {word}.")


if __name__ == "__main__":
    main()
