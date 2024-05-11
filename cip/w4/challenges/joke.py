"""
Code in Place 2024 https://codeinplace.stanford.edu/cip4
My notes: https://github.com/egalli64/pythonesque/cip

Program: Joke Bot
--------------------
If the user enters Joke then we will print out a single joke
"""

PROMPT = "What do you want? "
JOKE = "Here is a joke for you! Karel is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Karel returns with 13 liters of milk. The programmer asks why and Karel replies: 'because they had eggs'"
SORRY = "Sorry I only tell jokes"


def main():
    user_input = input(PROMPT)
    print(JOKE if user_input == "Joke" else SORRY)


if __name__ == "__main__":
    main()
