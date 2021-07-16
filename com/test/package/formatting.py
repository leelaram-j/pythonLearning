for i in range(1, 13):
    print("No. {0} squared is {1} and cube is {2}".format(i, i*i, i**3))

print()


for i in range(1, 13):
    print("No. {0:2} squared is {1:4} and cube is {2:4}".format(i, i*i, i**3))

print()

for i in range(1, 13):
    print("No. {0:2} squared is {1:<3} and cube is {2:^4}".format(i, i*i, i**3))