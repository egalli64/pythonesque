"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque cip folder

Nested Data: Recipe Book
- In the "recipes" dictionary each key is the name of a recipe
    - and each value is a dictionary with the minutes it takes and a list of ingredients.
- Keep asking for a recipe until the user presses enter instead of typing a name.
- For each recipe, print how long it takes and then each ingredient on its own line.
- If the recipe is not in the book, print a message instead.
"""


def main():
    recipes: dict[str, dict] = {
        "pancakes": {"minutes": 20, "ingredients": ["flour", "milk", "eggs"]},
        "salad": {"minutes": 10, "ingredients": ["lettuce", "tomato"]},
        "soup": {"minutes": 45, "ingredients": ["carrots", "onion", "broth"]},
    }

    while name := input("Which recipe? ").lower():
        if recipe := recipes.get(name, None):
            print(f"{name} takes {recipe['minutes']} minutes. You need:")
            for ingredient in recipe["ingredients"]:
                print("-", ingredient)
        else:
            print(f"There is no recipe for {name}.")


if __name__ == "__main__":
    main()
