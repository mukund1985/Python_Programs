# name = input("Please enter your name: ")
# age = int(input(" How old are you, {0}? ".format(name)))
# print(age)
#
# if age >= 18:  # Because we have used int, so we can use >= equal sign
#     print(" You are old enough to vote ")
#     print(" Please put an X in the box ")  # Which means that we can use multiple as well in on if / else condition
# else:
#     print(" Please come back in {} Years".format(18 - age))

# print(" Please guess a number between 1 and 10: ")
# guess = int(input())
# if guess < 5:
#     print("Please guess higher")
#     guess = int(input())
#     if guess == 5:
#         print("Well Done, You guessed it")
#     else:
#         print("Please try next time")
# elif guess > 5:
#     print("Please guess lower")
#     guess = int(input())
#     if guess == 5:
#         print("Well Done, You guessed it")
#     else:
#         print("Please try next time")
# else:
#     print(" Wow, You Guessed it")

# There can be better way to do this logic -

# print(" Please guess a number between 1 and 10: ")
# guess = int(input())
# if guess != 5:
#     if guess < 5:
#         print("Please guess higher")
#     else:  # Guess must be greater than 5
#         print("Please guess lower")
#     guess = int(input())
#     if guess == 5:
#         print("Well Done, You guessed it")
#     else:
#         print("Please try next time")
# else:
#     print("Wow, You guessed it")
#
# ####################################
#
# tree1 = "put your first tree name here"
# tree2 = "put your second tree name here"
#
# if tree1 == tree2:
#     print("The trees are the same")
# else:
#     print("The trees are different")
#
# ####################################

# age = int(input("How old are you?"))
# # # if (age >= 16) and (age <= 65): # Python gets stop as soon as it gets condition as false
# # if 16 <= age <= 65:
# #     print("Have a good day at work")
#
# if (age < 16) or (age > 65):   # While using or gets stop as soon as it gets condition as true
#     print("Enjoy your free time")
# else:
#     print("Have a good day at work")

###################################

# x = "False"  # X value is set false but still the o/p will be true because in python true is one and false is zero
# if x:
#     print("X is True")  # But in a condition any non-zero or non-empty values will evaluate to true

###################################

# age = int(input("How old are you? "))
# if not(age < 18):
#     print(" You are old enough to vote")
#     print("Please put x in the box")
# else:
#     print("Please come back in {0} Years".format(18 - age))

###################################

# parrot = "Norwegian Blue"
# letter = input("Enter a character: ")
#
# # if letter in parrot:
# #         print("Give me {}, Bob".format(letter))
# # else:
# # print(" I don't need that letter")
#
# if letter not in parrot:
#     print(" I don't need that letter")
# else:
#     print("Give me {}, Bob".format(letter))

###################################

# x = 1
# y = 1
#
# if x > y:
#     print(" x is greater than y")
# elif x < y:
#     print(" x is smaller than y")
# else:
#     print(" x is equals to y")

###################################

name = input(" Please Enter your Name: ")
age = int(input(" How old are you {0} ?".format(name)))

if 18 <= age < 31:
    print(" Hello {0}, Welcome to the Holiday !!" .format(name))
else:
    print(" Sorry {0} For {1} Years, entry is prohibitted ".format(name, age))

###################################