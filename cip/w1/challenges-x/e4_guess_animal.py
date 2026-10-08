"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque/cip

Guess My Animal
"""
from animal import get_random_animal
from ai import call_gpt

PROMPT = "Consider a {}. Answer yes or no to this question on it: {}"


def main():
    print("I am thinking of an animal.\nCan you guess what animal it is?")
    animal = get_random_animal()

    while True:
        question = input("Ask me a yes or no question: ")
        if question == animal:
            break
        else:
            result = call_gpt(PROMPT.format(animal, question))
            print(result)

    print("Correct!")


if __name__ == "__main__":
    main()
