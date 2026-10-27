"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque cip folder

Quiz Grader
"""


def main():
    key = ["b", "a", "d", "c", "a"]
    answers = ["b", "c", "d", "c", "b"]

    score = 0
    for i in range(len(key)):
        if answers[i] == key[i]:
            score += 1

    print(f"Your score: {score} / {len(key)}")


if __name__ == "__main__":
    main()
