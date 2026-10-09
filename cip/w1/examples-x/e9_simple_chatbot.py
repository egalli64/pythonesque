"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque/cip

Simple Chatbot: the user can continually ask questions to the AI model.
"""
from ai import call_gpt


def main():
    while True:
        message = input("You: ")

        if message != "bye":
            response = call_gpt(message)
            print(f"AI: {response}")
        else:
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
