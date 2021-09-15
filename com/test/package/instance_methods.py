# Instance Methods
class Student:
    name = "Lee"
    age = 25

    def printall(self, gender):
        print("name:",Student.name)
        print("age:",Student.age)
        print("gender:",gender)

o = Student()
o.printall("male")
Student.printall(o,"male")