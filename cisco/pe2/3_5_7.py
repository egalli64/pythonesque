"""
Cisco Network Academy
Python Essentials 2: https://skillsforall.com/course/python-essentials-2
My notes: https://github.com/egalli64/pythonesque - cisco/pe2 folder

PE2 Module 3 - Object-Oriented Programming
 Section 5 – OOP Fundamentals: Inheritance
 7. Single inheritance vs. multiple inheritance
 8. What is Method Resolution Order (MRO) and why is it that not all inheritances make sense? 
"""
print("SI example")


class Top:
    def m_top(self):
        print("top")


class Middle(Top):
    def m_middle(self):
        print("middle")


class Bottom(Middle):
    def m_bottom(self):
        print("bottom")


object = Bottom()
object.m_bottom()
object.m_middle()
object.m_top()

print("MI example")


class Bottom2(Middle, Top):
    def m_bottom(self):
        print("bottom 2")


object = Bottom2()
object.m_bottom()
object.m_middle()
object.m_top()

# Cannot create consistent method ordering!
# class Bottom3(Top, Middle):
#     def m_bottom(self):
#         print("bottom 2")
