"""
try:
    f = open("test1.txt", "r")
    print(f.read())
except Exception as e:
    print(e)
else:
    f.close()
"""

"""
try:
    f = open("test.txt", "r")
    print(f.readline())
    print(f.readline(5))
    print(f.readlines()) # this will convert the data into a list
except Exception as e:
    print(e)
else:
    f.close()
"""
try:
    f = open("test.txt", "r")
    for line in f:
        print(line)
except Exception as e:
    print(e)
else:
    f.close()