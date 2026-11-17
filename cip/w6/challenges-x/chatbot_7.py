"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque cip folder

Chatbot - step 7: Memory Budget
- Limit the bot memory to MAX_WORDS = 150.
- count_words(messages) returns the number of words in the content of every message.
- forget(messages) returns a new list with the system message, followed by everything after the 4 oldest messages.
  - If messages has fewer than 6 messages, return it unchanged.
- After appending the user's message, check whether count_words(messages) is more than MAX_WORDS.
  - If it is, set messages = forget(messages) and print how many messages and words are left.
"""
from ai import call_gpt

INDENT = "    "
PERSONALITY = "You are Emmett Brown from Back to the Future. Keep your replies short."
MAX_WORDS = 150


def count_words(messages: list) -> int:
    result = 0
    for message in messages:
        result += len(message["content"].split())
    return result


def forget(messages: list) -> list:
    if len(messages) < 6:
        return messages
    return messages[:1] + messages[5:]


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
                if count_words(messages) >= MAX_WORDS:
                    messages = forget(messages)

                    n = count_words(messages)
                    print(f"{INDENT}My memory was full! Now I remember {len(messages)} messages, {n} words.")

                prompt = format_messages(messages)
                response = call_gpt(prompt)
                messages.append(make_message("assistant", response))
                print("Bot:", response)


if __name__ == "__main__":
    main()
