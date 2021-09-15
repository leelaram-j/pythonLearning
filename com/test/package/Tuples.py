"""
Tuple in python
This is immutable
written inside ()
if at all you need to change a value inside this you need to convert tuple to a list and then change
the value
"""

a = (1, 2.5, True, "Ram")
print(a)

print(type(a))
print(a[1])
print(a[-1])
print(a[0:2])

b = list(a)
print(b)

b.append("Raja")
print(b)
print(type(b))

a = tuple(b)
print(a)
print(type(a))

for i in a:
    print(i)

if "Ram" in a:
    print("Ram is foung")
else:
    print("Ram is not there")

print(len(a))

a= (1)
print(type(a))

a = (1,)
print(type(a))

del a

a = (1, 2, 3, 4, 5)
b = (5, 6, 7, 8)

c = a + b
print(c)
print(c.count(5))

'''
Nested Tuples
'''
a = (1, 2, 3, 4, 5)
b = (5, 6, 7, 8)

c = (a,b)
print(c)
print(c[0])
print(c[0][1])

x = ('Joes',) * 10
print(x)

a = (1, 2, 7, 4)
print(min(a))
print(max(a))
