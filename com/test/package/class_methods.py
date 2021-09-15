class Student:
    name = "Lee"
    age = 25

    def printall():
        print("name:",Student.name)
        print("age:",Student.age)

print(Student.printall())

print(Student.__dict__)

print(getattr(Student, "printall"))
getattr(Student, "printall")()

Student.__dict__['printall']()