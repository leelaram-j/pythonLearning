age = 24
# print("My age is" + age + " years")
print("My age is " + str(age) + " years")
print("My age is {0} years".format(age))

'''replacemnet fields'''
print("Ther are {0} days in {1}, {2}, {3}, {4}, {5}, {6}, {7}"
      .format(31, "Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec"))

print("Jan: {2}, Feb: {0}, Mar: {2}, Apr: {1}".format(28, 30, 31))
print("""Jan: {2}
Feb: {0}    
Mar: {2}
Apr: {1}""".format(28, 30, 31))
