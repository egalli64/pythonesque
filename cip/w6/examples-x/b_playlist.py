"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque cip folder

Slices: Playlist
- Print the first and last songs in the playlist.
- Ask how many songs the user has time for, and print a list of that many songs from the start of the playlist.
- Remove those songs from the playlist, and print the songs that are left.
"""


def main():
    playlist = ["Morning Coffee", "Bus Window", "Rainy Day", "Dance Break", "Road Trip", "Goodnight"]

    print("First song:", playlist[0])
    print("Last song:", playlist[-1])

    count = int(input("How many songs do you have time for? "))
    print("You will hear:", playlist[:count])

    rest = playlist[count:]
    print("Saved for later:", rest)


if __name__ == "__main__":
    main()
