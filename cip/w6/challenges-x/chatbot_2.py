"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque cip folder

Chatbot - step 2: Keep a Record
- make_message(role, content) returns a message dictionary.
- In main, create an empty list called messages.
- Each time the user types a message, append a message to the list where the role is user.
- Each time the bot replies, append a message where the role is assistant.
messages = [
    {"role": "user", "content": "My name is Sam."},
    {"role": "assistant", "content": "Hi Sam, nice to meet you!"},
]
"""
from ai import call_gpt


def make_message(role: str, content: str) -> dict:
    return {"role": role, "content": content}


def main():
    messages = []
    print("Chat with the bot! (press Enter to quit)")

    while prompt := input("You: "):
        messages.append(make_message("user", prompt))
        response = call_gpt(prompt)
        messages.append(make_message("assistant", response))
        print(response)


if __name__ == "__main__":
    main()
