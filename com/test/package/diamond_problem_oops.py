"""
A is super parent
B, C inherits A
D inherits B, C

    A
  B   C
    D
"""

class A:
    def display(self):
        print("display of class A")

class B(A):
    def display(self):
        print("display of class B")

class C(A):
    def display(self):
        print("display of class C")

class D(B, C):
    def display(self):
        print("display of class D")

o = D()
o.display()

"""
First it will check if D has display function, if yes it will print. else it will
go to class B and check, if it is not there it will go to class C, if it is not there
even there, it will go to class A.
"""