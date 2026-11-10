"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque cip folder

Emoji Translator twist: Back to Words
reverse_dict()
"""


def build_emoji_dict():
    emoji_dict = {}
    word = input("Word: ")
    word = word.lower()
    while word != "":
        emoji = input(f"Emoji for {word}: ")
        emoji_dict[word] = emoji
        word = input("Word: ")
        word = word.lower()
    return emoji_dict


def print_emoji_dict(emoji_dict):
    for word in emoji_dict:
        emoji = emoji_dict[word]
        print(f"{word}: {emoji}")


def translate(sentence, emoji_dict):
    """twist: the dict is reversed: emoji to word"""
    result = ""

    words = sentence.split()
    for word in words:
        """twist: no use to lowercase an emoji"""
        result += emoji_dict[word] if word in emoji_dict else word
        result += " "

    return result


def reverse_dict(emojis):
    """twist"""
    result = {}

    for word, emoji in emojis.items():
        result[emoji] = word

    return result


def main():
    print("Let's build your emoji dictionary! Press enter when you are done.")
    emoji_dict = build_emoji_dict()
    num_words = len(emoji_dict)
    print(f"Words in your dictionary: {num_words}")
    print_emoji_dict(emoji_dict)
    # twist
    words = reverse_dict(emoji_dict)
    while message := input("Enter an emoji message: "):
        print(translate(message, words))


if __name__ == "__main__":
    main()
