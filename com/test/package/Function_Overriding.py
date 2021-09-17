# Function Over riding

class employee:
    def workinghrs(self):
        self.hrs = 50

    def printhrs(self):
        print("Total hrs: ", self.hrs)

class trainee(employee):
    def workinghrs(self):
        self.hrs = 60

    def resethrs(self):
        super().workinghrs()

e = trainee() # trainee class
e.workinghrs()
e.printhrs()

e1 = employee() # employee class
e1.workinghrs()
e1.printhrs()

# reset timing for trainee

e.resethrs()
e.printhrs()