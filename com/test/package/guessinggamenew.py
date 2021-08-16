import random

highest = 1000
answer = random.randint(1, highest) # TODO: Check this logic
guess = 0
counter =0
print(answer)
print("Please guess number between 1 and {}: ".format(highest))


while guess != answer:
    counter+=1
    if counter > 10:
        print("You have exceeded 10 tries so quitting")
        break
    guess = int(input()) # to convert to integer
    if guess == 0:
        break
    if guess == answer:
        print("You got it correctly")
        break
    else:
        if guess < answer:
            print("Please guess higher")
        else:
            print("Please guess lower")
        # guess = int(input())
        # if guess == answer:
        #     print("Well done, you guessed it correctly")
        # else:
        #     print("Sorry you have not guesses it correctly")
            #print("{} is the randomly generated number.".format(answer))
