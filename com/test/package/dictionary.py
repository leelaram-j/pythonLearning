'''
Dictionary data type:

similar to json, key value pair
we cannot have duplicate keys
can be indexed

'''


user = {
    "user1":{"name" : "Ram",
     "age" : 25,
     "isMarried" : True},
    "user2":{"name" : "Raja",
     "age" : 25,
     "isMarried" : False}
}

print(user)
print(type(user))
print(user["user1"])
print(user.get("user1"))
print(user.keys())
print(user.values())
print(user.items())

for x in user:
    print(x)
    print(user[x], "+++++")

for x in user.values():
    print(x)


for x in user.keys():
    print(x)

for x,y in user.items():
    print(x,y)

if "user1" in user:
   print("Present")
else:
    print("Not present")

for x in user.values():
    if "name" in x:
        print("Present")
        break
    else:
        print("Not present")

# change functions

user.update({"user1":{"name" : "Kamal","age" : 25,"isMarried" : True}})
print(user)

#user["user1"["age"]] = 45
# user.user1["age"] = 45
# print(user)

user.pop("user2")
print(user)

user.clear()
print(user)















