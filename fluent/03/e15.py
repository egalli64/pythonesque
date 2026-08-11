"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original code: https://github.com/fluentpython/example-code-2e/
My playground: https://github.com/egalli64/pythonesque/ fluent folder

set
"""
a_list = ["spam", "spam", "eggs", "spam", "bacon", "eggs"]
print("a list w/ duplicates:", a_list)
a_set = set(a_list)
print("let the set discard the duplicates:", a_set)
a_list_2 = list(a_set)
print("back to list w/o duplicates:", a_list_2)

# to preserve the original order, go through a map
a_dict_keys = dict.fromkeys(a_list).keys()
print(a_dict_keys)
a_list_3 = list(a_dict_keys)
print("back to list keeping order and w/o duplicates:", a_list_3)
