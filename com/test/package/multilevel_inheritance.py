class A:

    def printADetail(self):
        print("this is class A")

class B(A):
    def printBDetail(self):
        print("this is class B")

class C(B):
    def printCDetail(self):
        print("this is class C")

c = C()
c.printCDetail()
c.printBDetail()
c.printADetail()