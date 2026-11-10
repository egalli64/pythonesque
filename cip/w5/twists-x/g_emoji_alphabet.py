"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque cip folder

Emoji Translator twist: Emoji Alphabet
build_alphabet()
"""
# twist
LETTERS = ["a", "c", "e", "i", "o", "t"]
EMOJIS = ["🍎", "🐱", "🥚", "🍦", "🐙", "🌮"]


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
            result += emoji + " "
        else:
            result += word + " "
    return result


def build_alphabet(letters, emojis):
    """twist"""
    result = {}

    for letter, emoji in zip(letters, emojis):
        result[letter] = emoji

    return result


def main():
    # twist
    emoji = build_alphabet(LETTERS, EMOJIS)
    print_emoji_dict(emoji)


if __name__ == "__main__":
    main()
