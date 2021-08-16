# statements in else will run only if the while loop is completely run, it is stopped in between
# else statements will not work.

i = 1
while i <= 5:
    print(i)
    i += 1
else:
    print("Loop Completed.")

i = 1
for i in range(i, 10, 1):
    print(i)
else:
    print("For Loop COmpleted.")