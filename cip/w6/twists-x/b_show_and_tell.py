"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque cip folder

Chatbot twist: Show and Tell
Fix the bug: "show" and "peek" should work in the same way
"""
from ai import call_gpt

INDENT = "    "
PERSONALITY = "You are super sassy. Keep replies short."


def make_message(role, content):
    return {"role": role, "content": content}


def peek(messages):
    print(f"{INDENT}The record has {len(messages)} messages:")
    for message in messages:
        print(f"{INDENT}{message['role']}: {message['content']}")


def format_messages(messages):
    result = ""
    for message in messages:
        if message["role"] == "user":
            result += f"User: {message['content']}\n"
        elif message["role"] == "system":
            result += f"Instructions: {message['content']}\n\n"
        else:
            result += f"Assistant: {message['content']}\n"
    result += "Assistant:"
    return result


def main():
    print("Chat with the bot! (press Enter to quit)")
    messages = [make_message("system", PERSONALITY)]

    user_content = input("You: ")

    while user_content != "":
        # fix using "in" instead of "or"
        if user_content in ("peek", "show"):
            peek(messages)
        else:
            user_message = make_message("user", user_content)
            messages.append(user_message)

            prompt = format_messages(messages)
            bot_content = call_gpt(prompt)
            print(f"Bot: {bot_content}")

            bot_message = make_message("assistant", bot_content)
            messages.append(bot_message)

        user_content = input("You: ")


if __name__ == "__main__":
    main()
