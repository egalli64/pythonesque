"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque/cip

Translation Practice, Again
"""
from ai import call_gpt

PROMPT = "Translate {} from English to {}. Give me just the translated word."


def main():
    lang = input("What language do you want to practice? ")

    while True:
        word = input("Type a word in English, or done to quit: ")
        if word != "done":
            user_translation = input(f"Type the word in {lang}: ")
            gpt_translation = call_gpt(PROMPT.format(word, lang))

            if user_translation.lower() == gpt_translation.lower():
                print("Wahoo! You and GPT agreed on the translation.")
            else:
                print(f"Oh no! GPT said that the translation is {gpt_translation}")
        else:
            print("Nice practicing with you!")
            break


if __name__ == "__main__":
    main()
