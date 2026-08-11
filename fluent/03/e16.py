"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original code: https://github.com/fluentpython/example-code-2e/
My playground: https://github.com/egalli64/pythonesque/ fluent folder

set intersection
"""
needles = {42, 27, 1024}
haystack = {x for x in range(100)}

# Example 3-12. Count occurrences of needles in a haystack, both of them are set
found = len(needles & haystack)
print(f"there are {found} needles in the haystack (by intersection)")

found = 0
for needle in needles:
    if needle in haystack:
        found += 1
print(f"there are {found} needles in the haystack (by loop and check)")
