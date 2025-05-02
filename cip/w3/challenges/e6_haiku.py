"""
Code in Place 2025 https://codeinplace.stanford.edu/cip5
My notes: https://github.com/egalli64/pythonesque/cip

Haiku Generator
"""

from ai import call_gpt


def main():
    name = input("Enter your name: ")
    topic = input("Enter a topic: ")
    response = call_gpt(f"Generate a haiku about {name} and {topic}")
    print(response)


if __name__ == "__main__":
    main()
