"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque/cip

Hello, Detective: Ask for the player's name at the start. Then use their name in the game's messages.
"""
from animal import get_random_animal
from ai import call_gpt

PROMPT = "Consider a {}. Answer yes or no to this question on it: {}"


def main():
    user = input("What's your name? ")  # added
    animal = get_random_animal()
    print(f"I am thinking of an animal, {user}.\nCan you guess what animal it is?")  # changed

    question = input("Ask me a yes or no question: ")
    prompt = f"We are playing twenty questions and the answer is {animal}. The user has asked the following yes or no question: {question}. Please respond with exactly Yes, No, or Correct if they guess the animal exactly. Do not say anything else."
    gpt_response = call_gpt(prompt)

    while gpt_response != "Correct":
        print(f"{gpt_response}.")

        question = input("Ask me a yes or no question: ")
        prompt = f"We are playing twenty questions and the answer is {animal}. The user has asked the following yes or no question: {question}. Please respond with exactly Yes, No, or Correct if they guess the animal exactly. Do not say anything else."
        gpt_response = call_gpt(prompt)

    print(f"Correct! Nice work, Detective {user}!")  # changed


if __name__ == "__main__":
    main()
