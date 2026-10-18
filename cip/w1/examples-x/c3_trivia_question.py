"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque cip folder

Calling GPT - Trivia Question
"""
from ai import call_gpt


def main():
    topic = input("What topic? ")
    question = call_gpt(f"Ask one trivia question about {topic}.")
    print(f"Trivia question: {question}")


if __name__ == "__main__":
    main()
