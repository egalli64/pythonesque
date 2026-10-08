"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque/cip

AI Joke Bot: Write a program which prompts the user to type the required affirmation correctly.
Milestone 3: Make different jokes.
"""
from ai import call_gpt

PROMPT = "Tell me a joke"


def main():
    print("Hello! I am an AI joke bot.")

    joke = None
    while True:
        more_jokes = input("Do you want to hear a joke? Type yes or no: ")
        if more_jokes == "yes":
            prompt = f"{PROMPT}\nYou already told me: {joke}" if joke else PROMPT
            joke = call_gpt(prompt)
            print(joke)
        else:
            break


if __name__ == "__main__":
    main()
