"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque cip folder

No Repeats twist
"""
from words import get_random_word

NUM_ATTEMPTS = 6


def main():
    print("Welcome to Wordle!")

    secret_word = get_random_word()

    # twist
    history = []

    for attempt in range(NUM_ATTEMPTS):
        guess = input("Enter your guess: ").lower()
        # twist begin
        while guess in history:
            print("You already guessed that one!")
            guess = input("Enter your guess: ").lower()
        history.append(guess)
        #twist end
        while len(guess) != 5:
            print("Please enter a 5-letter word.")
            guess = input("Enter your guess: ").lower()

        remaining_letters = []
        for i in range(5):
            remaining_letters.append(secret_word[i])

        result = []
        for i in range(5):
            if secret_word[i] == guess[i]:
                result.append("G")
                remaining_letters.remove(secret_word[i])
            else:
                result.append("B")

        for i in range(5):
            if result[i] == "B":
                if guess[i] in remaining_letters:
                    result[i] = "Y"
                    remaining_letters.remove(guess[i])

        result_str = "Result:"

        for i in range(5):
            if result[i] == "G":
                result_str = f"{result_str} [{guess[i]}]"
            if result[i] == "Y":
                result_str = f"{result_str} ({guess[i]})"
            if result[i] == "B":
                result_str = f"{result_str} {guess[i]}"
        print(result_str)

        if secret_word == guess:
            print(f"Congratulations! You guessed the word in {attempt + 1} tries!")
            break

        if attempt == NUM_ATTEMPTS - 1:
            print(f"Better luck next time! The correct word was '{secret_word}'.")


if __name__ == "__main__":
    main()
