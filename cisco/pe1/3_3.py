"""
Cisco Network Academy
Python Essentials 1: https://skillsforall.com/course/python-essentials-1
My notes: https://github.com/egalli64/pythonesque - cisco/pe1 folder

PE1: Module 3 Section 3 Logic and bit operations in Python
"""
# 3.3.2 Logical expressions
var = 1
print("Is var larger than 0?", var > 0)
print("Is var _not_ less or equal to 0 (same)?", not (var <= 0))

print("Is var _not equal_ to 0?", var != 0)
print("Is var _not_ _equal to_ 0?", not (var == 0))

# De Morgan's laws
print("The negation of a conjunction is the disjunction of the negations")
for p in {False, True}:
    for q in {False, True}:
        print(f"p: {p}, q: {q} ->", (not (p and q)) == ((not p) or (not q)))

print("The negation of a disjunction is the conjunction of the negations")
for p in {False, True}:
    for q in {False, True}:
        print(f"p: {p}, q: {q} ->", (not (p or q)) == ((not p) and (not q)))

# 3.3.3 Logical values vs. single bits
i = 42
# in boolean context 0 == false, not 0 == true
j = not i
k = not not i
print(i, j, k)

# 3.3.4 Bitwise operators
i = 15          # 0..001111
j = 22          # 0..010110
print(i & j)    # 0..000110 - AND
print(i | j)    # 0..011111 - OR
print(i ^ j)    # 0..011001 - XOR
print(~i)       # 1..110000 - NOT
print(i >> 1)   # 0..000111 - right shift
print(i << 2)   # 0..111100 - left shift
