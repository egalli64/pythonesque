"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque cip folder

Vowel Hider: step 2, main
"""
VOWELS = "aeiou"


def hide_vowels(message: str) -> str:
    result = ""

    for c in message:
        if c in VOWELS:
            result += '*'
        else:
            result += c

    return result


def main():
    message = input("Enter a secret: ")
    print(hide_vowels(message))


if __name__ == "__main__":
    main()
