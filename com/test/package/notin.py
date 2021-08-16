activity = input("What would you like to do today? ")
if "cinema" not in activity:
    print("But i want to go to cinema")

if "cinema" not in activity.casefold():
    print("But i want to go to cinema")

#https://docs.python.org/3/library/stdtypes.html
#Use this link to refer documentation so that we can view other functions in string