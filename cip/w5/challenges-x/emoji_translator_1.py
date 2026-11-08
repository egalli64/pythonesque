"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque cip folder

Emoji Translator - step 1
build_emoji_dict()
"""


def main():
    print("Let's build your emoji dictionary! Press enter when you are done.")
    emoji_dict = build_emoji_dict()
    print("Words in your dictionary:", len(emoji_dict))


def build_emoji_dict():
    result = {}

    while word := input("Word: ").lower():
        emoji = input(f"Emoji for {word}: ")
        result[word] = emoji

    return result


if __name__ == "__main__":
    main()
