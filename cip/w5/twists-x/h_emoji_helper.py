"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque cip folder

Emoji Translator twist: Emoji Helper
Using AI support
"""
from ai import call_gpt


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
    result = ""

    words = sentence.split()
    for word in words:
        lower_word = word.lower()
        if lower_word in emoji_dict:
            emoji = emoji_dict[lower_word]
        else:
            # twist
            emoji = call_gpt(f"Reply with just one emoji for the word {word}.")
            emoji_dict[lower_word] = emoji

        result += emoji
        result += " "

    return result


def main():
    print("Let's build your emoji dictionary! Press enter when you are done.")
    emoji_dict = build_emoji_dict()
    num_words = len(emoji_dict)
    print(f"Words in your dictionary: {num_words}")
    print_emoji_dict(emoji_dict)
    sentence = input("Enter a sentence: ")
    while sentence != "":
        translation = translate(sentence, emoji_dict)
        print(translation)
        sentence = input("Enter a sentence: ")

    # twist: final balance
    num_words = len(emoji_dict)
    print(f"Words in your dictionary: {num_words}")
    print_emoji_dict(emoji_dict)


if __name__ == "__main__":
    main()
