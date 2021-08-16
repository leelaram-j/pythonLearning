for i in range(1, 21):
    print("i value is {}".format(i))


for i in range(10):
    print("i value is {}".format(i))

for i in range(0, 10, 2):
    print("i value is {}".format(i))

print("-------------")

for i in range(10, 0, -2):
    print("i value is {}".format(i))

#range(1,10) --> here the start value is included and the end value is not#

for i in range(1, 13):
    for j in range(1, 13):
        print("{0} * {1} = {2}".format(j, i, i*j))
    print("----------------------------")