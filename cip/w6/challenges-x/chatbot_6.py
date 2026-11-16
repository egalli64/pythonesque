"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque cip folder

Chatbot - step 6: Rewind
- rewind(messages) returns a slice of messages without its last two messages.
  - Don't drop the system message!
- invoke rewind() when the user prompt for "rewind".
  - reset the messages with its result.
  - print how many messages are left.
"""
from ai import call_gpt

INDENT = "    "
PERSONALITY = "You are Emmett Brown from Back to the Future. Keep your replies short."


def peek(messages: list):
    print(f"{INDENT}The record has {len(messages)} messages:")
    for message in messages:
        print(f"{INDENT}{message['role']}: {message['content']}")


def make_message(role: str, content: str) -> dict:
    return {"role": role, "content": content}


def format_messages(messages: list):
    result = ""

    for message in messages:
        role = message['role']
        if role == "system":
            result += f"Instructions: {message['content']}\n\n"
        else:
            result += f"{role.capitalize()}: {message['content']}\n"
    result += "Assistant:"

    return result


def rewind(messages: list) -> list:
    if len(messages) > 2:
        return messages[:-2]
    return messages


def main():
    messages = [make_message("system", PERSONALITY)]
    print("Chat with the bot! (press Enter to quit)")

    while prompt := input("You: "):
        match prompt:
            case "peek":
                peek(messages)
            case "rewind":
                messages = rewind(messages)
                print(f"Rewound! The record has {len(messages)} messages.")
            case _:
                messages.append(make_message("user", prompt))
                prompt = format_messages(messages)
                response = call_gpt(prompt)
                messages.append(make_message("assistant", response))
                print(response)


if __name__ == "__main__":
    main()
