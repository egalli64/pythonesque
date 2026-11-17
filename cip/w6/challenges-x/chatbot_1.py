"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque cip folder

Chatbot - step 1: Goldfish Bot
"""
from ai import call_gpt


def main():
    print("Chat with the bot! (press Enter to quit)")

    while prompt := input("You: "):
        response = call_gpt(prompt)
        print("Bot:", response)


if __name__ == "__main__":
    main()
