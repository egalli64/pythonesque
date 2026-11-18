"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque cip folder

Chatbot twist: Try again
The "again" command throws away the bot's last reply and asks for a new one.
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


def bot_answer(messages):
    """Try Again twist support"""
    prompt = format_messages(messages)
    bot_content = call_gpt(prompt)
    print(f"Bot: {bot_content}")

    bot_message = make_message("assistant", bot_content)
    messages.append(bot_message)


def main():
    print("Chat with the bot! (press Enter to quit)")
    messages = [make_message("system", PERSONALITY)]

    user_content = input("You: ")

    while user_content != "":
        if user_content == "peek":
            peek(messages)
        elif user_content == "again":
            # Try Again twist
            if len(messages) == 1:
                print(f"{INDENT}Nothing to try again yet.")
            else:
                messages = messages[:-1]
                bot_answer(messages)
        else:
            user_message = make_message("user", user_content)
            messages.append(user_message)
            # avoid duplication for Try Again twist
            bot_answer(messages)

        user_content = input("You: ")


if __name__ == "__main__":
    main()
