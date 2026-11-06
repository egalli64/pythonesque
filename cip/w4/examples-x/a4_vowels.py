"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque cip folder

Combo: Is It a Vowel?, Count the Vowels
"""
VOWELS = "aeiou"
LETTER_CHECKER = False


def is_vowel(letter):
    return letter in VOWELS


def count_vowels(word):
    return sum(map(is_vowel, word))


def main():
    if LETTER_CHECKER:
        letter = input("Enter a letter: ")
        maybe_not = "" if is_vowel(letter) else " not"
        print(f"{letter} is{maybe_not} a vowel.")
    else:
        word = input("Enter a word: ")
        print(f"{word} has {count_vowels(word)} vowels.")


if __name__ == "__main__":
    main()
