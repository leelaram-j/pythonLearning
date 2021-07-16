answer = 5

print("Please guess number between 1 and 10: ")
guess = int(input()) # to convert to integer

# if guess < answer:
#     print("please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("You did not guess correctly")
# elif guess > answer:
#     print("please guess lower")
#     guess = int(input())
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("You did not guess correctly")
# else:
#     print("you got it first time")



# if guess != answer:
#     if guess < answer:
#         print("Please guess higher")
#     else:
#         print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it correctly")
#     else:
#         print("Sorry you have not guesses it correctly")
# else:
#     print("You got it first time")


if guess == answer:
    print("You got it first time")
else:
    if guess < answer:
        print("Please guess higher")
    else:
        print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it correctly")
    else:
        print("Sorry you have not guesses it correctly")
