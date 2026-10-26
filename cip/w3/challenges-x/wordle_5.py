"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque cip folder

Wordle: step 5, polish
"""
from words import get_random_word

NUM_ATTEMPTS = 6


def main() -> None:
    print("Welcome to Wordle!")
    # 1. secret word is different every game
    secret = get_random_word()

    for j in range(NUM_ATTEMPTS):
        # 2. accept any capitalization
        guess = input("Enter your guess: ").lower()

        # 3. the guess must be exactly a five-letter string
        while len(guess) != 5:
            print("Please enter a 5-letter word.")
            guess = input("Enter your guess: ").lower()

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

    print(f"Better luck next time! The correct word was '{secret}'.")


if __name__ == "__main__":
    main()
