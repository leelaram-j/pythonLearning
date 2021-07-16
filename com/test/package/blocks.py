for i in range(1,13):
    print("No {} squared is  {} and cubed is {}".format(i, i*i, i*i*i))

print("------------------------------------------------------------------")

for i in range(1,13):
    print("No {:2} squared is  {:3} and cubed is {:4}".format(i, i*i, i*i*i))

print("------------------------------------------------------------------")

name = input("Please enter your name ")
age = int(input("How old are you {0} " .format(name))) # this specifies only number is entered anything other tha that
                                                    # will throw an error
print(age)

if age == 900:
    print("You are not a human")
elif age >= 18:
    print("You are old enough to vote")
else:
    print("You are not old enough to vote. Please come in {}".format(18-age))