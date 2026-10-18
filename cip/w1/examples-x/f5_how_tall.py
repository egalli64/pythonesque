"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque cip folder

Numbers - How Tall Is It?
"""
from ai import call_gpt


def main():
    landmark = input("Name a landmark: ")
    user_height = float(input("How tall are you in meters? "))

    prompt = f"Tell me the height of {landmark} in meters, just the number."
    landmark_height = float(call_gpt(prompt))

    print(f"The {landmark} is {landmark_height} meters tall.")
    print(f"That is about {round(landmark_height / user_height, 2)} of you stacked up!")


if __name__ == "__main__":
    main()
