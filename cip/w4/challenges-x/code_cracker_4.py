"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque cip folder

Code Cracker: step 4, crack
"""
ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def shift_letter(letter: str, n: int) -> str:
    index = (ALPHABET.find(letter) + n) % len(ALPHABET)
    return ALPHABET[index]


def encode(message: str, n: int) -> str:
    result = ""

    for letter in message:
        if letter in ALPHABET:
            result += shift_letter(letter, n)
        else:
            result += letter

    return result


def decode(message: str, n: int) -> str:
    return encode(message, -n)


def crack(message: str) -> None:
    for i in range(1, 26):
        print(f"Shift {i}:", decode(message, i))


def main():
    print("Welcome to the Code Machine!")
    message = input("Enter a message: ")
    crack(message)


if __name__ == "__main__":
    main()
