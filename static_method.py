# static method in python

class student:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def printDetail(self):
        print("Name: ", self._name, " Age: ", self._age)

    @staticmethod
    def welcome():
        print("Welcome to python")

s1 = student("Ram", 25)
s1.printDetail()
s1.welcome()

s2 = student("Lee", 30)
s2.printDetail()
s2.welcome()