"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque cip folder

Movie Night
- Start with an empty list of movies.
- Ask for movie and votes until no movie input. Store each movie as a dictionary with a title and votes.
- Print how many movies there were and which one got the most votes.
- If there were no movies, print a message instead.
"""


def make_movie(title: str, votes: int) -> dict:
    return {"title": title, "votes": votes}


def main() -> None:
    movies: list = []

    while title := input("Movie: "):
        votes = int(input(f"Votes for {title}: "))
        movies.append(make_movie(title, votes))

    if not movies:
        print("No movies were entered")
    else:
        selected = movies[0]
        for i in range(1, len(movies)):
            if movies[i]["votes"] > selected["votes"]:
                selected = movies[i]

        print(f"{len(movies)} movies. Tonight we are watching {selected['title']}!")


if __name__ == "__main__":
    main()
