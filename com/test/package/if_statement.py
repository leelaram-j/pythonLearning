





















"""
0   no fine
1-5     0.5
5-10    1
10-30   5
>30 Memebership cancel
"""


n = int(input("Enter a number of days: "))
if n == 0:
    print("No fine")
elif n >= 1 and n <=5:
    print("Fine: ", n * 0.5)
elif n > 5 and n <=10:
    print("Fine: ", n * 1)
elif n > 10 and n <=30:
    print("Fine: ", n * 5)
else:
    print("Membership Cancel" )

"""
nested if is if inside if
"""