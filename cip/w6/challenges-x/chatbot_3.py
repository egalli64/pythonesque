"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque cip folder

Chatbot - step 3: Peek at the Record
- peek(messages) prints how many messages are in the list, then each message's role and content.
  - Start every line it prints with INDENT
- In main, when the user types peek, call peek(messages) instead of sending anything to call_gpt.
- Do not add peek to messages.
"""
from ai import call_gpt

INDENT = "    "


def peek(messages: list):
    print(f"{INDENT}The record has {len(messages)} messages:")
    for message in messages:
        print(f"{INDENT}{message['role']}: {message['content']}")


def make_message(role: str, content: str) -> dict:
    return {"role": role, "content": content}


def main():
    messages = []
    print("Chat with the bot! (press Enter to quit)")

    while prompt := input("You: "):
        if prompt == "peek":
            peek(messages)
        else:
            messages.append(make_message("user", prompt))
            response = call_gpt(prompt)
            messages.append(make_message("assistant", response))
            print("Bot:", response)


if __name__ == "__main__":
    main()
