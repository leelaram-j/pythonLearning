a = 10
b = 20

print(a+b)

a = "Lee"
b = "Ram"

print(a+b)

class addition:
    def __init__(self, a):
        self.a = a

    def __add__(o1, o2):
        return o1.a + o2.a

object1 = addition(10)
object2 = addition(20)

print("Total: ", (object1 + object2))

class subtract:
    def __init__(self, a):
        self.a = a

    def __sub__(o1, o2):
        return o1.a - o2.a

object1 = subtract(10)
object2 = subtract(5)

print("Total: ", (object1 - object2))

object1 = subtract("LEEEL")
object2 = subtract("LEE")

print("Total: ", (object1 - object2))

"""
Arithmetic Operators
 
Operator	Expression	Internally

Addition	p1 + p2	p1.__add__(p2)
Subtraction	p1 - p2	p1.__sub__(p2)
Multiplication	p1 * p2	p1.__mul__(p2)
Power	p1 ** p2	p1.__pow__(p2)
Division	p1 / p2	p1.__truediv__(p2)
Floor Division	p1 // p2	p1.__floordiv__(p2)
Remainder (modulo)	p1 % p2	p1.__mod__(p2)
Bitwise Left Shift	p1 << p2	p1.__lshift__(p2)
Bitwise Right Shift	p1 >> p2	p1.__rshift__(p2)
Bitwise AND	p1 & p2	p1.__and__(p2)
Bitwise OR	p1 | p2	p1.__or__(p2)
Bitwise XOR	p1 ^ p2	p1.__xor__(p2)
Bitwise NOT	~p1	p1.__invert__()

Comparison operators:

Operator	Expression	Internally

Less than	p1 < p2	p1.__lt__(p2)
Less than or equal to	p1 <= p2	p1.__le__(p2)
Equal to	p1 == p2	p1.__eq__(p2)
Not equal to	p1 != p2	p1.__ne__(p2)
Greater than	p1 > p2	p1.__gt__(p2)
Greater than or equal to	p1 >= p2	p1.__ge__(p2)
 
 """