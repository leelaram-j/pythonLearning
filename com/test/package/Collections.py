"""""
Lists mutable
index access

tuple
ordered
immutable
can have duplicate entries

sets
un ordered and declared in curly braces
no index access
no duplciate entries

dictionary
{}
mutable
general purpose collection
"""""

""""
list
indexing
ordered
starts and ends with []
"""

fruits = ['apple', 'mango', 'kiwi', 'banana']
print(fruits[1:6])

fruits = ['apple', 'mango', 'kiwi', 'banana', 2, 4, 80, 80.7]
print(fruits[1:10])
fruits.append(20)
print(fruits)
fruits.insert(5, 400)
print(fruits)
fruits.reverse()
print(fruits)

""""
dictionary ~ to map
starts with curly braces
uses key value pair
"""

courses = {1: "python",
           2: "data science",
           "third": "hello"}

print(courses)
print(courses["third"])

""""
tuple -- order cannot be changed
can add duplicates
they are immutable
can be accessed through index
starts ends with ()
"""

animals = (10, 12, 20, 'tiger', 'liion', 'tiger')
print(animals)
print(animals[4])
print(animals.count("tiger"))

"""""
Set - un ordered, insertion sequence not preserved.
no duplicates
does not support indexing
starts ends with {}
"""""

setin = {"a", "a", 00, 23, 45.4, "tiger", "lion", 23}
print(setin)

"""""
range gets the value between the given values
"""""

print(range(10))
print(list(range(10)))

a = [1, 2, 3, 4]
b = {5, 6, 7, 8, 9}
c = [a, b]
print(c)

"""""
specialized collection module called collections
it is built in


1) namedtuple()
2) Chainmap
3) dequeue
4) Counter
5) OrderedDict
6) defaultdict
7) UserDict
8) UserList
9) UserString
"""""

"""""
namedtuple
access index specific
it returns a tuple with named value for each element in tuple

Details = (name="edurekha", course="python", course2 = "data science"

namedtuple takes only 2 params -- remember that
a = namedtuple('courses', 'name,technology')
for second param, u need to pass the values in comma separated
"""""

from collections import namedtuple

a = namedtuple('courses', 'name,technology')
s = a('datascience', 'python')
print(s)
s = a._make(['artifical intelligence', 'python'])

"""""
Deque 
optimized list to perform insertion and deletion easily
Deque(['l','e','e'])
"""""

from collections import deque

a = ['e', 'd', 'u', 'r', 'e', 'k', 'a']
print(a)
d = deque(a)
d.append('zoom')

print(d)

d.appendleft('python')

print(d)

c = d.pop()
b = d.popleft()
print("************")
print(c)
print(b)
print(d)

"""""
Chainmap is a dictionary like class for creating a single view of multiple mappings
rturns several other dictionary
combine multiple dictionary
"""""

from collections import ChainMap

a = {1: "edurekha", 2: "python"}
b = {3: "ML", 4: "AI"}

a1 = ChainMap(a, b)
print(a1)
print(a1.keys())
print(a1.values())


"""""
Counter is a dictionary subclass for counting hashable objcects
"""""

from collections import Counter

a = [1,1,2,3,4,4,3,4,3,5,6,7,8,9,6,9]
c = Counter(a)
print(c)
print(list(c.elements()))

print (c.most_common()) # this returns the count in order of which has more count

sub = {2:1, 6:1}
print(c.subtract(sub))
print (c.most_common())

"""""
OrderedDict
ordereddict is dictionary subclass which remembers the order in which the entries were done.
whcih remember in which order entries were added.
even if the values of key the position is not forgotten
"""""

from collections import OrderedDict

d = OrderedDict()
d[1] = 'l'
d[2] = 'e'
d[3] = 'r'

print(d)
print(d.keys())
print(d.items())

d[1] = 'o'
print(d)