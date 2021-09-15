class user:
    course = 'Java'

o = user()
print(user.__dict__)
print(user.course) # class attribute

print(o.__dict__)
print(o.course) # instance attribute

o.course = 'C++'
print(o.__dict__)
print(o.course)
print(user.course)

o2 = user()
print(o2.course)