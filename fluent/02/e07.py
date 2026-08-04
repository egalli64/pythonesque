"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original file: https://github.com/fluentpython/example-code-2e/blob/master/02-array-seq/array-seq.ipynb
My playground: https://github.com/egalli64/pythonesque/ fluent folder

Comparing Tuple and List Methods
"""
a_tuple = (1, 2, 3)
print("A tuple:", a_tuple)

a_list = [1, 2, 3]
print("A list:", a_list)

# tuple/list __add__
print("tuple + another tuple:", a_tuple + (4, 5))
print("list + another list:", a_list + [4, 5])

# list __iadd__
b_list = [1, 2]
b_list += a_list
print("+=", b_list)

# list append
b_list.append(42)
print("Append:", b_list)

# list clear
b_list.clear()
print("Clear:", b_list)

# tuple/list __contains__
print("check if an element is in a tuple:", 2 in a_tuple)
print("check if an element is in a list:", 2 in a_list)

# list (shallow) copy
c_list = a_list.copy()
print("A shallow copy:", c_list, id(c_list) == id(a_list), id(c_list[0]) == id(a_list[0]))

# tuple/list count
print("Count 1 in a tuple:", a_tuple.count(1))
print("Count 42 in a list:", a_list.count(42))

# list __delitem__
b_list = a_list.copy() * 2
print(f"calling del on 1 for {b_list} gives:")
del b_list[1]
print(b_list)
print(f"calling del on [1:3] for {b_list} gives:")
del b_list[1:3]
print(b_list)

# list extends
print(f"extends {b_list} with {a_tuple} gives:")
b_list.extend(a_tuple)
print(b_list)

# tuple/list __getitem__
print("get item 1 from tuple:", a_tuple[1])
print("get item 1 from list:", a_list[1])

# tuple/list index
print("Index of (first) 1 in a tuple:", a_tuple.index(1))
print("Index of (first) 1 in a list:", a_list.index(1))

# list insert
print(f"inserting 42 in {b_list} before item in position 3 gives:")
b_list.insert(3, 42)
print(b_list)

# tuple/list __iter__
print("Iterating on tuple", a_tuple)
for x in a_tuple:
    print("\t", x)
print("Iterating on list", a_list)
for x in a_list:
    print("\t", x)

# tuple/list __len__
print(f"len of {a_tuple} is", len(a_tuple))
print(f"len of {a_list} is", len(a_list))

# tuple/list __mul__
print(f"{a_tuple} * 3 is", a_tuple * 3)
print(f"{a_list} * 3 is", a_list * 3)

# list __imul__
print(f"{b_list} *= 2 is")
b_list *= 2
print("\t", b_list)

# tuple/list __rmul__
print(f"3 * {a_tuple} is", 3 * a_tuple)
print(f"3 * {a_list} is", 3 * a_list)

# list pop
print(f"Calling pop on {b_list} gives {b_list.pop()} for {b_list}")

# list remove
b_list.remove(42)
print("Remove the first 42 from the list:", b_list)

# list reverse
b_list.reverse()
print("Reverse a list:", b_list)

# list __reversed__
print("Reverse iterating on list")
for x in reversed(a_list): print("\t", x)
print("Tuple does not required a specialized __reversed__ for reversing:")
for x in reversed(a_tuple): print("\t", x)

# list __setitem__
b_list[5] = 42
print("Set 42 in position 5:", b_list)

# list sort
b_list.sort()
print("Sorted list:", b_list)
