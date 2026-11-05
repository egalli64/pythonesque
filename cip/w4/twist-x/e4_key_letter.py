"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque cip folder

Key Letter twist - use a letter as shift
"""
ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def shift_letter(letter, n):
    position = ALPHABET.find(letter)
    new_position = (position + n) % len(ALPHABET)
    return ALPHABET[new_position]


def encode(message, n):
    result = ""
    for letter in message:
        if letter in ALPHABET:
            result += shift_letter(letter, n)
        else:
            result += letter
    return result


def decode(message, n):
    return encode(message, -n)


def main():
    print("Welcome to the Code Machine!")
    message = input("Enter a message: ")
    # begin twist
    key = input("Enter a key letter: ")
    shift = ord(key) - ord("a")
    secret = encode(message, shift)
    print("Secret:", secret)
    # end twist


if __name__ == "__main__":
    main()
