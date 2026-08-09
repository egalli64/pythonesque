"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original code: https://github.com/fluentpython/example-code-2e/
My playground: https://github.com/egalli64/pythonesque/ fluent folder

Inserting or Updating Mutable Values
"""
a_dict = {"a": [42, 12], "b": [5, 4], "c": [3]}
print(a_dict)

# long-winded way
for key in "cd":
    if key not in a_dict:
        a_dict[key] = []
    a_dict[key].append(99)

print(a_dict)

# setdefault()
for key in "de":
    a_dict.setdefault(key, []).append(42)
print(a_dict)
