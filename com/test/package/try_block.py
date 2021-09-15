# try block is useful for runtine errors

# print( 10/0)

'''
try:
    a = 10/0
except Exception as e:
    print(e)
'''

try:
    a = 10/0
except Exception as e:
    print(e)
else:
    print("value is",a)
finally:
    print("Thats all for today")

print(dir(locals()['__builtins__'])) # to print all exception details
print(len(dir(locals()['__builtins__']))) # to print all exception details

# name error exception
'''
based on variable name
'''

try:
    print(b)
except NameError as e:
    print(e)
#

try:
    print(10/0)
except ZeroDivisionError as e:
    print(e)

try:
    a = int("Lee")
    print(a)
except ValueError as e:
    print(e)

try:
    a = [10,20,30,40]
    print(a[10])
except IndexError as e:
    print(e)

try:
    f = open("test.txt")
except FileNotFoundError:
    print("File not found")
except ZeroDivisionError:
    print("Denominator cannot be zero")
else:
    print(f.read())

























