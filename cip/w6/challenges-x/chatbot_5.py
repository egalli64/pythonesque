"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque cip folder

Chatbot - step 5: Give It a Personality
- Define the bot PERSONALITY: who it is, how it talks, and what it knows. Tell it to keep replies short.
- initialize messages with a system message for the personality
- format_messages treats system message as Instructions:  plus its content, followed by a blank line (two \n).
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


def main():
    messages = [make_message("system", PERSONALITY)]
    print("Chat with the bot! (press Enter to quit)")

    while prompt := input("You: "):
        if prompt == "peek":
            peek(messages)
        else:
            messages.append(make_message("user", prompt))
            prompt = format_messages(messages)
            response = call_gpt(prompt)
            messages.append(make_message("assistant", response))
            print("Bot:", response)


if __name__ == "__main__":
    main()
