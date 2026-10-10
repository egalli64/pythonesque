"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque/cip

Special Guest: Ask for the player's name at the start. If it's your section leader's name, roll out the red carpet!
"""
from animal import get_random_animal
from ai import call_gpt


def main():
    animal = get_random_animal()

    # add: start
    name = input("What's your name? ")
    if name.lower() == "sam":
        print(f"Welcome, VIP {name}! The red carpet is ready for you.")
    else:
        print(f"Welcome, {name}!")
    # add: end

    print("I am thinking of an animal.")
    print("Can you guess what animal it is?")

    question = input("Ask me a yes or no question: ")

    prompt = f"We are playing twenty questions and the answer is {animal}. The user has asked the following yes or no question: {question}. Please respond with exactly Yes, No, or Correct if they guess the animal exactly. Do not say anything else."
    gpt_response = call_gpt(prompt)

    while gpt_response != "Correct":
        print(f"{gpt_response}.")

        question = input("Ask me a yes or no question: ")

        prompt = f"We are playing twenty questions and the answer is {animal}. The user has asked the following yes or no question: {question}. Please respond with exactly Yes, No, or Correct if they guess the animal exactly. Do not say anything else."
        gpt_response = call_gpt(prompt)

    print("Correct!")


if __name__ == "__main__":
    main()
