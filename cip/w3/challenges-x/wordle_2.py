"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque cip folder

Wordle: step 2, yellow matches
"""


# not used in steps 1 and 2
# from words import get_random_word
# NUM_ATTEMPTS = 6


def main() -> None:
    print("Welcome to Wordle!")
    secret = "candy"
    guess = input("Enter your guess: ")  # five-letter word assumed

    # 1: for Yellow check
    remaining_letters = list(secret)
    result = []

    for i in range(5):
        if guess[i] == secret[i]:
            result += "G"
            # 2: remove match
            remaining_letters.remove(guess[i])
        else:
            result += "B"

    # 3. check for yellow chars
    for i in range(5):
        if result[i] == "B" and guess[i] in remaining_letters:
            result[i] = "Y"

    print("Result:", " ".join(result))


if __name__ == "__main__":
    main()
