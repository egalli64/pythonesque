"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque/cip

Victory Lap: Ask GPT for an emoji of the animal and print it after "Correct!"
"""
from animal import get_random_animal
from ai import call_gpt


def main():
    animal = get_random_animal()

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

    emoji = call_gpt(f"Reply with only one emoji that shows a {animal}.") # add
    print(emoji) # add


if __name__ == "__main__":
    main()
