"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original file: https://github.com/fluentpython/example-code-2e/blob/master/02-array-seq/array-seq.ipynb
My playground: https://github.com/egalli64/pythonesque/ fluent folder

List Comprehensions and Readability
"""
# Example 2-1. Build a list of Unicode codepoints from a string
symbols = '$¢£¥€¤'
codes = []

for symbol in symbols:
    codes.append(ord(symbol))

if value := globals().get("symbol"):
    print("Loop variable is leaked in the global scope:", value)
else:
    print("Unexpected!")

print("The last symbol is:", symbol)  # noqa

print("The symbols:", symbols)
print("The symbols as Unicode codepoints:", codes)

# Example 2-2. Build a list of Unicode codepoints from a string, using a listcomp
alt_codes = [ord(x) for x in symbols]
print("The symbols as Unicode codepoints (by listcomp):", alt_codes)

if globals().get("x"):
    print("Unexpected!")
else:
    print("Listcomp variable are not leaked (anymore) out of scope!")

# However, the walrus operator behave in its own peculiar way
codes = [last := ord(c) for c in symbols]

if globals().get("last"):
    print("Last symbol is accessible outside the listcomp")
else:
    print("Unexpected!")

if globals().get("c"):
    print("Unexpected!")
else:
    print("The variable c is local to the listcomp")
