# Property Decorator

class user:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # self.msg = self.name + " is " + str(self.age) + " years old."

    #     def msg(self):
    #         return self.name + " is " + str(self.age) + " years old."
    #
    # o = user("Lee", 30)
    # print(o.name)
    # print(o.age)
    # print(o.msg())
    # o.age = 45
    # print(o.msg())

    # in the above the msg is considered as a function and it should be used as such.
    # if we need to use it as an attribute we need to @property annotation, as seen below

    @property
    def msg(self):
        return self.name + " is " + str(self.age) + " years old."


o = user("Lee", 30)
print(o.name)
print(o.age)
print(o.msg)
o.age = 45
print(o.msg)
