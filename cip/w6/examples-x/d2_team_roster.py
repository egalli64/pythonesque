"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque cip folder

Nested Data: Team Roster
- Given the teams dictionary
- Keep asking for a new player's name until the user presses enter instead of typing a name.
- For each player, ask which team they want and add them to that team's list.
- If there is no such team, print a message instead.
- At the end, print each team, how many players it has, and who they are.
"""


def main():
    teams = {
        "red": ["Ana", "Ben"],
        "blue": ["Cleo"],
    }

    while player := input("New player's name: "):
        team_name = input("Which team, red or blue? ")
        if team := teams.get(team_name):
            team.append(player)
        else:
            print(f"There is no {team_name} team.")

    for name, team in teams.items():
        print(f"{name} team has {len(team)} players:", team)


if __name__ == "__main__":
    main()
