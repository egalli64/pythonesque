"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque cip folder

Chatbot - step 4: Give It a Memory
- format_messages(messages) returns the conversation as one string.
  - Put each message on its own line, starting with "User: " for user messages and "Assistant: " for the bot's messages.
  - Then add "Assistant:" to the end of the string so the AI knows it is its turn to talk.
- before call_gpt(prompt) set prompt to format_messages(messages)
"""
from ai import call_gpt

INDENT = "    "


def peek(messages: list):
    print(f"{INDENT}The record has {len(messages)} messages:")
    for message in messages:
        print(f"{INDENT}{message['role']}: {message['content']}")


def make_message(role: str, content: str) -> dict:
    return {"role": role, "content": content}


def format_messages(messages: list):
    result = ""

    for message in messages:
        role = message['role'].capitalize()  # just for the cip tester
        result += f"{role}: {message['content']}\n"
    result += "Assistant:"

    return result


def main():
    messages = []
    print("Chat with the bot! (press Enter to quit)")

    while prompt := input("You: "):
        if prompt == "peek":
            peek(messages)
        else:
            messages.append(make_message("User", prompt))
            prompt = format_messages(messages)
            response = call_gpt(prompt)
            messages.append(make_message("Assistant", response))
            print(response)


if __name__ == "__main__":
    main()
