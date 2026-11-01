"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque cip folder

Code Cracker: step 1, shift_letter
"""
ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def shift_letter(letter: str, n: int) -> str:
    index = (ALPHABET.find(letter) + n) % len(ALPHABET)
    return ALPHABET[index]


def main():
    print("Welcome to the Code Machine!")
    letter = input("Enter a letter: ")
    shift = int(input("Enter a shift: "))
    encoded_letter = shift_letter(letter, shift)
    print(f"{letter} shifted by {shift} is {encoded_letter}")


if __name__ == "__main__":
    main()
