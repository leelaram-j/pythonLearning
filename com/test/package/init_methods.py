# this is similar to constructor

class user:
    def __init__(self, name):
        print("Called when new instance is created")
        self.name = name

    def printall(self):
        print("Name:", self.name)

o = user("Lee") # constructor method, used during run time initialization of variables
o.printall()
print(o.__dict__)

o1 = user("Ram")
o1.printall()
print(o1.__dict__)

print(user.__dict__)

