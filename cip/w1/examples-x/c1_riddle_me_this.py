"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque cip folder

Calling GPT - Riddle Me This
"""
from ai import call_gpt


def main():
    topic = input("Enter a topic: ")
    prompt = f"Tell me a one-liner riddle about {topic}."
    riddle = call_gpt(prompt)
    print(riddle)


if __name__ == "__main__":
    main()
