"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque cip folder

Is It a Vowel?
"""
VOWELS = "aeiou"


def is_vowel(letter):
    return letter in VOWELS


def main():
    letter = input("Enter a letter: ")
    maybe_not = "" if is_vowel(letter) else " not"
    print(f"{letter} is{maybe_not} a vowel")

if __name__ == "__main__":
    main()
