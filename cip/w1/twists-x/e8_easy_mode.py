"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque/cip

Easy Mode: GPT adds a small clue to every answer.
"""
from animal import get_random_animal
from ai import call_gpt


def main():
    # begin: easy mode
    mode = input("Easy mode? Type yes or no: ")
    if mode == "yes":
        rules = "If they write the animal name, respond exactly 'Correct'. Otherwise, answer Yes or No, then add a short clue, like: No, but it has stripes."
    else:
        rules = "Respond with exactly Yes, No, or Correct if they guess the animal exactly. Do not say anything else."
    # end: easy mode

    animal = get_random_animal()

    print("I am thinking of an animal.")
    print("Can you guess what animal it is?")

    question = input("Ask me a yes or no question: ")

    # add specific mode rules
    prompt = f"We are playing twenty questions and the answer is {animal}. The user has asked the following yes or no question: {question}. {rules}"
    gpt_response = call_gpt(prompt)

    while gpt_response != "Correct":
        print(f"{gpt_response}")

        question = input("Ask me a yes or no question: ")

        prompt = f"We are playing twenty questions and the answer is {animal}. The user has asked the following yes or no question: {question}. {rules}"
        gpt_response = call_gpt(prompt)

    print("Correct!")


if __name__ == "__main__":
    main()
