"""
Code in Place 2025 https://codeinplace.stanford.edu/cip5
My notes: https://github.com/egalli64/pythonesque/cip

Program: Quizzlet
Loop over the provided dictionary asking for the key translation, comparing the answer with the value
"""


def main():
    translations = {
        "hello": "hola",
        "dog": "perro",
        "cat": "gato",
        "well": "bien",
        "us": "nos",
        "nothing": "nada",
        "house": "casa",
        "time": "tiempo",
    }

    ok = 0
    for key, value in translations.items():
        translation = input(f"What is the Spanish translation for {key}? ")
        if translation == value:
            ok += 1
            print("That is correct!")
        else:
            print(f"That is incorrect, the Spanish translation for {key} is {value}.")
        print()

    print(f"You got {ok}/{len(translations)} words correct, come study again soon!")


if __name__ == "__main__":
    main()
