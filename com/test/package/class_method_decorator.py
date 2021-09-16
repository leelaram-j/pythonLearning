class student:
    count = 0
    def __init__(self, name, age):
        self._name = name
        self._age = age
        student.count += 1

    def printDetail(self):
        print("Name: ", self._name, " Age: ", self._age)

    @classmethod # this method belongs to a class, using this we are getting teh count of objects.
    def total(cls):
        return cls.count

o = student("Ram", 25)
o.printDetail()

a = student("Lee", 30)
a.printDetail()

print("Total Admission: ", student.total())
print("Total Admission: ", o.total())