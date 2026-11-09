"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque cip folder

Emoji Translator twist: Starter Pack
food_pack(), animal_pack()
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


def food_pack():
    """Twist"""
    return {"pizza": "🍕", "taco": "🌮", "apple": "🍎"}


def animal_pack():
    """Twist"""
    return {"cat": "🐱", "dog": "🐶", "fish": "🐟"}


def main():
    # Twist
    pack = input("Pick a pack (food or animals): ").lower()
    emojis = food_pack() if pack == "food" else animal_pack()

    print("Words in your dictionary:", len(emojis))
    print_emoji_dict(emojis)

    while sentence := input("Enter a sentence: "):
        translation = translate(sentence, emojis)
        print(translation)


if __name__ == "__main__":
    main()
