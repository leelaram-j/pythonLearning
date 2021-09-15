class Student():
    name = "Ram"
    age = 25

# using getattr metod to get variables  inside class

print(getattr(Student, 'name'))
print(getattr(Student, 'age'))
print(getattr(Student, 'gender', "No Such attribute found"))

# Dot Method

print(Student.age)
print(Student.name)

# setattr
setattr(Student, 'name', "Lee")
print(Student.name)

setattr(Student, 'gender', 'Male')
print(Student.gender)

Student.city = "Chennai"
print(Student.city)

print(Student.__dict__)

# deleting attributes
delattr(Student, 'city')
print(Student.__dict__)

del Student.gender
print(Student.__dict__)



























