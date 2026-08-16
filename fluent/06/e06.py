"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original code: https://github.com/fluentpython/example-code-2e/
My playground: https://github.com/egalli64/pythonesque/ fluent folder

By default, copy is shallow
"""
l1 = [3, [66, 55, 44], (7, 8, 9)]
print("original list:", l1)

l2 = list(l1)
print("shallow copy of the original list:", l2)

l1.append(100)
print("appending an item to the original list ha no effect on its shallow copy:", l2)

l1[1].remove(55)
print("when a sublist from the original list changes:", l1)
print("also the shallow copy sees the change:", l2)

l2[1] += [33, 22]
l2[2] += (10, 11)
print("the shallow copy, after += on both sublist and sub-tuple:", l2)
print("the original list sees the change on the sublist, but keeps reference to the original sub-tuple", l1)
