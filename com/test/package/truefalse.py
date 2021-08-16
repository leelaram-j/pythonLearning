day = "Saturday"
temperature = 28
raining = False

if day == "Saturday" and temperature > 27 and not raining:
    print("Go swimming")
else:
    print("learn Python")

    # learn to use paranthesis when using and or in same sentence

#0 is evaluted to false when used in condition
if 0:
    print("true")
else:
    print("false")

name  = input("enter your name")
if name:
    print("hello {}".format(name))
else:
    print("enter proper name")