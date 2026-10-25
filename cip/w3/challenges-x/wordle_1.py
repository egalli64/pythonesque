"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque cip folder

Wordle: step 1, exact matches
"""


# not used in step 1
# from words import get_random_word
# NUM_ATTEMPTS = 6


def main() -> None:
    # 1
    print("Welcome to Wordle!")

    # 2: fixed secret word
    secret = "candy"

    # 3: assume input is exactly 5 chars
    guess = input("Enter your guess: ")

    # 4: G(ood) or B(ad) for each char
    result = []
    for i in range(5):
        if guess[i] == secret[i]:
            result += "G"
        else:
            result += "B"
    print("Result:", " ".join(result))


if __name__ == "__main__":
    main()
