"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque cip folder

Chatbot twist: Pick a Bot
Ask the user to pick a bot personality from the BOTS list
"""
from ai import call_gpt

INDENT = "    "
# Pick a Bot twist
BOTS = [
    {"name": "Captain Kit", "personality": "You are Captain Kit, a pirate. Keep replies short."},
    {"name": "Chef Rosa", "personality": "You are Chef Rosa, a very dramatic chef. Keep replies short."},
    {"name": "Beep", "personality": "You are Beep, a very literal robot. Keep replies short."},
]


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


def pick_a_bot():
    """Pick a Bot twist"""
    for i, bot in enumerate(BOTS):
        print(f"{i}: {bot['name']}")
    selected_bot = int(input("Pick a bot: ")) % len(BOTS)
    bot = BOTS[selected_bot]
    return [make_message("system", bot["personality"])], bot["name"]


def main():
    print("Chat with the bot! (press Enter to quit)")
    # Pick a Bot twist
    messages, bot_name = pick_a_bot()

    user_content = input("You: ")

    while user_content != "":
        if user_content == "peek":
            peek(messages)
        else:
            user_message = make_message("user", user_content)
            messages.append(user_message)

            prompt = format_messages(messages)
            bot_content = call_gpt(prompt)
            # Pick a Bot twist
            print(f"{bot_name}: {bot_content}")

            bot_message = make_message("assistant", bot_content)
            messages.append(bot_message)

        user_content = input("You: ")


if __name__ == "__main__":
    main()
