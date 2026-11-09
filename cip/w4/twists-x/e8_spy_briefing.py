"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque cip folder

Spy Briefing twist: AI based
"""
from random import randint
from ai import call_gpt

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


def crack(message):
    for i in range(25):
        shift = i + 1
        decoded_message = decode(message, shift)
        print(f"Shift {shift}: {decoded_message}")


def spy_message(topic):
    prompt = f"Give me a short lowercase-only spy message about {topic}."
    return call_gpt(prompt)


def main():
    print("Welcome to the Code Machine!")
    topic = input("Enter a topic: ")
    message = spy_message(topic)
    shift = randint(1, 25)
    secret = encode(message, shift)
    print("Secret briefing:", secret)
    input("Can anyone crack it? Press enter to find out. ")
    crack(secret)


if __name__ == "__main__":
    main()
