parrot = "Blue"

letter = input("Enter a character: ")

if letter in parrot:
    print("{} is in {}". format(letter, parrot))
else:
    print("No need of this letter")