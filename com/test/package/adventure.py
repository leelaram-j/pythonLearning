available_exits = ["north", "south", "east", "west"]

choosen_exit = ""
while choosen_exit not in available_exits:
    choosen_exit = input("Please choose a value ")
    if choosen_exit.casefold() == "quit":
        print("Game Over")
        break

print("arent you glad you came out ")