# Property Decortor Setter Getter

# Adding _ to variable name makes the variable private

class Student:
    def __init__(self, total):
        self._total = total

    def average(self):
        return self._total / 5.0

    @property # since we have set this as property we can access this directly without ()
    def total(self):
        return self._total

    @total.setter # since we have set this as property we can access this directly without (), even assign values directly
    def total(self, t):
        if t < 0 or t > 500:
            print("Enter right value")
        else:
            self._total = t

o = Student(450)
print(o.total)
print(o.average())

o.total = 250
print(o.total)
print(o.average())