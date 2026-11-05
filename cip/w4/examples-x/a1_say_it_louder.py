"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque cip folder

Say It Louder
"""
PUNCH_LINE = "and I mean it"


def shout(word):
    return word.upper() + "!"


def main():
    word = input("What should I shout? ")
    print(shout(word))
    print(shout(PUNCH_LINE))


if __name__ == "__main__":
    main()
