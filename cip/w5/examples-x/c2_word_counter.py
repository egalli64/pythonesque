"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque cip folder

Word Counter
"""


def main():
    sentence = input("Enter a sentence: ").lower()
    raw_counter = {}

    for word in sentence.split():
        if word not in raw_counter:
            raw_counter[word] = 1
        else:
            raw_counter[word] += 1

    for word, count in raw_counter.items():
        print(f"{word}: {count}")


if __name__ == "__main__":
    main()
