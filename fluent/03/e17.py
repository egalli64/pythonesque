"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original code: https://github.com/fluentpython/example-code-2e/
My playground: https://github.com/egalli64/pythonesque/ fluent folder

set comprehension
"""
from unicodedata import name

some_signs = {chr(i) for i in range(32, 256) if "SIGN" in name(chr(i), "")}
print(some_signs)

# just out of curiosity
for i in range(32, 256):
    current_name = name(chr(i), "")
    if "SIGN" in current_name:
        print(i, chr(i), current_name)
