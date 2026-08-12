"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original code: https://github.com/fluentpython/example-code-2e/
My playground: https://github.com/egalli64/pythonesque/ fluent folder

Handling Text Files
"""
FILENAME = "cafe.tmp"
# Example 4-8. A platform encoding issue
# accordingly to the current platform it could be a problem, or not
open(FILENAME, "w", encoding="utf_8").write("café")
print("Text persisted in", FILENAME)

cafe = open(FILENAME).read()
print("It could be wrong:", cafe)

cafe = open(FILENAME, encoding="UTF-8").read()
print("Explicitly using UTF-8:", cafe)
