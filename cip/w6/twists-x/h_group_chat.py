"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque cip folder

Chatbot twist: Group Chat
Each bot in the BOTS list is going to reply to the user
"""
from ai import call_gpt

INDENT = "    "
# Group Chat twist
BOTS = [
    {"name": "Captain Kit", "personality": "You are Captain Kit, a pirate. Keep replies short, put no character cue in your answer."},
    {"name": "Chef Rosa", "personality": "You are Chef Rosa, a very dramatic chef. Keep replies short, put no character cue in your answer."},
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


def bots_reply(messages):
    """Group Chat twist"""
    for bot in BOTS:
        system_message = make_message("system", bot["personality"])
        bot_messages = [system_message] + messages
        prompt = format_messages(bot_messages)
        bot_content = call_gpt(prompt)
        reply = f"{bot['name']}: {bot_content}"
        print(reply)
        bot_message = make_message("assistant", reply)
        messages.append(bot_message)


def main():
    # Group Chat twist
    print("Chat with the bots! (press Enter to quit)")
    messages = []

    user_content = input("You: ")

    while user_content != "":
        if user_content == "peek":
            peek(messages)
        else:
            user_message = make_message("user", user_content)
            messages.append(user_message)

            # Group Chat twist
            bots_reply(messages)

        user_content = input("You: ")


if __name__ == "__main__":
    main()
