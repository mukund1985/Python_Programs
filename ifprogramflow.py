# name = input("Please enter your name: ")
# age = int(input(" How old are you, {0}? ".format(name)))
# print(age)
#
# if age >= 18:  # Because we have used int, so we can use >= equal sign
#     print(" You are old enough to vote ")
#     print(" Please put an X in the box ")  # Which means that we can use multiple as well in on if / else condition
# else:
#     print(" Please come back in {} Years".format(18 - age))

print(" Please guess a number between 1 and 10: ")
guess = int(input())

if guess <5:
    print("Please guess higher")
    guess = int(input())
    if guess == 5:
        print("Well Done, You guessed it")
    else:
        print("Please try next time")
elif guess >5:
    print("Please guess lower")
    guess = int(input())
    if guess == 5:
        print("Well Done, You guessed it")
    else:
        print("Please try next time")

else:
    print(" Wow, You Guessed it")