def sampleFunction():
    print("Hellow World")

sampleFunction()

# No return type without argument in python

'''
def add():
    a = int(input("Enter a value: "))
    b = int(input("Enter b value: "))
    c = a + b
    print("total", c)

add()
'''

# No return type with parameter

'''
def subs(a, b):
    c = a - b
    print("total", c)

subs(10, 5)
'''

# Return type without argument

'''
def mul():
    a = int(input("Enter a value: "))
    b = int(input("Enter b value: "))
    c =  a * b
    return c

total = mul()
print(total)
'''

# Return type with argument

'''
def div(a,b):
    c = a / b
    return c

x = div(10,5)
print(x)
'''

# Arbitary arguments function in python (*)

def class10(*students):
    print(students)
    for student in students:
        print(student)

class10("Ram", "Sam", "Kumar")

# Keyword argument function in python

def message(name, age):
    print(name, " age is ", age)

message(age=25, name="kumar")

# Arbitary Keyword Argument function in python

def bioData(** data):
    print(data)

bioData(name="Ram", age = 25, gender = "Male")

# Default parameter function in python

def user(name , city="Salem"):
    print(name, " is from ", city)

user("Ram", "Chennai")
user("Kumar")

# Passing a list as an argument in function

def total(marks):
    return sum(marks)

print(total([10,10,10,10,10]))

# creating dummy function

def test(x):
    pass

test(10)


# Recursive Function

def factorial(x):
    if x==1:
        return 1
    else:
        return x * factorial(x-1)

print(factorial(5)) # output 120

# Lambda functions

# single arument

a =10
c = lambda a:a+50
print(c(5)) # output 55

# multiple argument

c = lambda a,b : a*b
print(c(10,12)) # output 120






















