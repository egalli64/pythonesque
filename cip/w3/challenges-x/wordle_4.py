"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque cip folder

Wordle: step 4, six attempts
"""

# not used in steps 1, 2, 3, and 4
# from words import get_random_word
NUM_ATTEMPTS = 6


def main() -> None:
    print("Welcome to Wordle!")
    secret = "candy"

    # 1. a few attempts are allowed
    for j in range(NUM_ATTEMPTS):
        guess = input("Enter your guess: ")  # five-letter word assumed

        remaining_letters = list(secret)
        result = []

        guessed = 0
        for i in range(5):
            if guess[i] == secret[i]:
                result.append(f"[{secret[i]}]")
                remaining_letters.remove(guess[i])
                guessed += 1
            else:
                result += "B"

        for i in range(5):
            if result[i] == "B":
                if guess[i] in remaining_letters:
                    result[i] = f"({guess[i]})"
                else:
                    result[i] = f"{guess[i]}"

        print("Result:", " ".join(result))
        if guessed == 5:
            # 2. stop looping when guessed
            print(f"Congratulations! You guessed the word in {j + 1} tries!")
            return

    # 3. can't guess
    print(f"Better luck next time! The correct word was '{secret}'.")


if __name__ == "__main__":
    main()
