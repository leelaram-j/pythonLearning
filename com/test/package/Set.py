'''
Set
Set is simialr to mathematics uion intersection
it is collection of un ordered and un indexed data type
data location cannot be predicted.
it is written in {}
you cannot change values after inserting it in set
duplicate values are not allowed in set

'''


name = {'Ram', 'Sam', 'Ravi'}
print(name)
print(type(name))

# Access values using for loop
for names in name:
    print(names)

# Adding new element

name.add('Sara')
print(name)

# Update another set of data

a = {'kumar', 'Sundar', 'Suresh'}
name.update(a)
print(name)

# discard vs remove -> discard will not throw error if the element is not there

name.discard('Sara')
print(name)

name.remove('Sundar')
print(name)

name.pop()
print(name)

name.clear()
print(name)

# del name
# print(name)

a = {1, 2, 3, 4}
b = {'a', 'b', 'c', 'd'}

c= a.union(b)
print(c)

a.update(b)
print(a)

a = {1,2,3,4,5}
b = {5,6,7,8,9}

c = a.intersection(b)
print(c)

a.intersection_update(b)
print(a)

a = {1,2,3,4,5}
b = {5,6,7,8,9}

c = a.symmetric_difference(b)
print(c)

a = {1,2,3,4}
b = {5,6,7,8,9}

c = a.isdisjoint(b)
print(c)

c = a.issubset(b)
print(c)

c= a.issuperset(b)
print(c)





















