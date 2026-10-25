"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque cip folder

Wordle: step 3, format the output
"""


# not used in steps 1, 2, and 3
# from words import get_random_word
# NUM_ATTEMPTS = 6


def main() -> None:
    print("Welcome to Wordle!")
    secret = "candy"
    guess = input("Enter your guess: ")  # five-letter word assumed

    remaining_letters = list(secret)
    result = []

    for i in range(5):
        if guess[i] == secret[i]:
            # 1. right letter in square brackets
            result.append(f"[{secret[i]}]")
            remaining_letters.remove(guess[i])
        else:
            result += "B"

    for i in range(5):
        if result[i] == "B":
            if guess[i] in remaining_letters:
                # 2. wrong position letter in round brackets
                result[i] = f"({guess[i]})"
            else:
                # 3. wrong letter
                result[i] = f"{guess[i]}"

    print("Result:", " ".join(result))


if __name__ == "__main__":
    main()
