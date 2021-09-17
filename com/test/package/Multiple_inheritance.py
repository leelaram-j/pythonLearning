class father:
    def printFName(self):
        print("Father Name is Ram")

    def chess(self):
        print("learning chess from father")


class mother:
    def printMName(self):
        print("Mother Name is Leela")

    def chess(self):
        print("learning chess from Mother")


class son(father, mother):
    def ride(self):
        print("Driving cycle")


o = son()
o.printFName()
o.printMName()
o.chess()
o.ride()

"""
 if there are 2 functions with same name in parent classes, then the function from first parent 
 will be taken. if function from second parent is needed to be called we need to interchange 
 the order of calling.
""" 