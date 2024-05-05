"""
Code in Place 2024 https://codeinplace.stanford.edu/cip4
My notes: https://github.com/egalli64/pythonesque/cip

Tiny mad libs: given an adjective, a noun, and a verb, print a sentence with those words in it
"""

START = "Code in Place is fun. I learned to program and used Python to make my "


def main():
    adjective = input("Please type an adjective and press enter. ")
    noun = input("Please type a noun and press enter. ")
    verb = input("Please type a verb and press enter. ")

    print(START + adjective + " " + noun + " " + verb + "!")


if __name__ == "__main__":
    main()
