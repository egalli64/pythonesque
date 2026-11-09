"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque cip folder

Mirror Alphabet twist: 'a' becomes 'z', 'b' becomes 'y', ...
"""
ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def mirror(message):
    result = ""
    for letter in message:
        if letter in ALPHABET:
            result += ALPHABET[-(ALPHABET.find(letter) + 1)]
        else:
            result += letter
    return result


def main():
    print("Welcome to the Code Machine!")
    message = input("Enter a message: ")
    # begin twist
    mirrored = mirror(message)
    print("Mirrored:", mirrored)
    print("Mirrored again:", mirror(mirrored))
    # end twist


if __name__ == "__main__":
    main()
