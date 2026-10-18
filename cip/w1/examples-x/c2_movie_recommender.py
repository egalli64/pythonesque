"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque cip folder

Calling GPT - Movie Recommender
"""
from ai import call_gpt


def main():
    genre = input("What genre are you in the mood for? ")
    movie = call_gpt(f"Tell me just the title of a {genre} movie.")
    print(f"Here is your movie: {movie}")


if __name__ == "__main__":
    main()
