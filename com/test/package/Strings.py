str = "we win"
print(str)

print("w")
print("e")
print()
print("w")
print("i")
print("n")

str = "parrot"

print()

for i in range(0,len(str)):
    print(str[i])

parrot = "Norwegian Blue"

# slices remember that [:] right side will not be included
print(parrot[0:14])
print(parrot[:1])
print(parrot[0:1])
print(parrot[10:14])
print(parrot[10:])
print(parrot[:])


letters = "abcdefghijklmnopqrstuvwxyz"
print(letters[3:])
print(letters[4:14])



#we can also use negative index to access the values based on index


print(parrot[0:6:3])

# this is an idiom for reversing n python  [::-1]
backwards = letters[::-1]
print(backwards)

print(letters[16:13:-1])
print(letters[-22::-1])
print(letters[:17:-1])
print(letters[-4:])
print(letters[:1])


