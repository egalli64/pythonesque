"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque cip folder

Emoji Translator - step 3
translate()
"""


def build_emoji_dict():
    result = {}

    while word := input("Word: ").lower():
        emoji = input(f"Emoji for {word}: ")
        result[word] = emoji

    return result


def print_emoji_dict(emojis):
    print("Words in your dictionary:", len(emojis))
    for name, emoji in emojis.items():
        print(f"{name}: {emoji}")


def translate(sentence, emojis):
    result = ""

    for word in sentence.split():
        key = word.lower()
        if key not in emojis:
            result += word
        else:
            result += emojis[key]

        result += " "

    return result


def main():
    print("Let's build your emoji dictionary! Press enter when you are done.")

    emoji_dict = build_emoji_dict()
    print_emoji_dict(emoji_dict)

    sentence = input("Enter a sentence: ")
    print(translate(sentence, emoji_dict))


if __name__ == "__main__":
    main()
