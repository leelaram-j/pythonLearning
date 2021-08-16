# for i in range(10):
#     print("i is now {}".format(i))

i = 0
while i < 10:
    if i % 2 == 0:
        i += 1
        continue
    print("i is now {}".format(i))
    i += 1


i = 1
while i < 10:
    if i == 6:
        break
    print(i)
    i += 1

