"""
List in python
written inside []
sequence type, index based starts from 0
mutable

"""

a = [1, 2, 3, 4, 5]
print(a)
print(type(a))

print(a[1])

# array slicing
print("Slicing")
print(a[0:3])
print(a[2:])
print(a[:3])

print("-------------")
a = [1, "sample", True, 10.45, [1, 2, 3, 4]]
print(a)
print(type(a))
print(type(a[1]))
print(a[4][2])
print("-------------")
b = a.copy()
print(b)
print(a)
a.clear()
print(a)

print("-------------")

a = [10, 20, 30, 10, 20, 40, 50, 10]
print(a.count(10))
print(a.index(20))
print(len(a))
print(max(a))
print(min(a))

print(a)
a.pop(0) # values are removed based on index
print(a)

a.remove(10) # values are removed based on actual value
print(a)

print("-------------")

names = ["Ram"]
print(names)
names.append("Sam")
names.append("Kumar")
print(names)

name2 = ["Sara", "Mike"]
names.extend(name2)
print(names)

names.insert(0, "Kiran")
print(names)


print("-------------")
print(list(range(5)))
print(list("leelaram"))


a = [10,50,100, 25, 85]
print(a)
a.sort()
print(a)
a.sort(reverse=True)
print(a)

a = ["z", "a", "y", "b"]
a.sort()
print(a)

a = ["mango", "zebra", "apple"]
a.sort()
print(a)

a = ["mangoes", "zebra", "apples"]
a.sort(key=len)
print(a)




















