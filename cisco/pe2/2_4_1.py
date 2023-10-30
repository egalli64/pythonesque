"""
Cisco Network Academy
Python Essentials 2: https://skillsforall.com/course/python-essentials-2
My notes: https://github.com/egalli64/pythonesque - cisco/pe2 folder

PE2 Module 2 - Strings, List, Exceptions
 Section 4 – String in action
 1. Comparing strings
"""
sa1 = 'alpha'
sa2 = 'alpha'
sa3 = 'Alpha'
print(f'{sa1} == {sa2}?', sa1 == sa2)
print(f'{sa1} != {sa3}?', sa1 != sa3)

sa4 = 'alphabet'
print(f'{sa1} < {sa4}?', sa1 < sa4)

sb1 = 'beta'
sb2 = 'Beta'
print(f'{sb1} > {sb2}?', sb1 > sb2)

sc1 = '10'
sc2 = '010'
print(f'{sc1} > {sc2}?', sc1 > sc2)

print("Object of different types are different, regardless of their similarity")
sc3 = 10
print(f'{sc1} (str) != {sc3} (int)?', sc1 != sc3)
try:
    sc1 > sc3
except TypeError:
    print("'>' could be applied only between compatible types")
