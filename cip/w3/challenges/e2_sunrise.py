"""
Code in Place 2025 https://codeinplace.stanford.edu/cip5
My notes: https://github.com/egalli64/pythonesque/cip

Sunrise Fill-in-the-Blanks
The user will enter three words (a color, an adjective and a goal).
We will then turn them into a one sentence story.
"""


def main():
    color = input("A color: ")
    adjective = input("An adjective: ")
    goal = input("A goal you would like to achieve: ")

    print(f"At dawn the sky turned {color}, and the air felt {adjective}.", end="")
    print(f"I decided today I will finally {goal}.")


if __name__ == "__main__":
    main()
