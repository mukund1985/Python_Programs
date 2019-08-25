#  For Loop:-  It actually takes a range of values and assign them one by one to a variable and then executes a block of
#  code once for each value. In Python For loop like - for i, taking each of the values in the
#  following sequence, do something.
#  In Python - Different Approach for for loop that python uses makes it really powerful, incredibly powerful, but also
#  very flexible.


#  We will be printing at the values from 1 to 20

# for i in range(1, 20):
#     print(" i is now {0}".format(i))
#
# number = "9,223,372,036,854,775,807"
# for i in range(0, len(number)):  # Function len is an abbreviation for length and returns the length of a string
#     print(number[i])  # How many characters actually exist in that string. Loop will print each element of
# String and by using the square bracket, it is printing the character at position i. we started on the first time
# position i, i had the value of zero, so position zero is 9, next time it is , and so on.

##################################

# number = "9,223,372,036,854,775,807"
# for i in range(0, len(number)):
#     if number[i] in '0123456789':
#         print(number[i], end='\t')

##################################
# Now if we wanted to use a number that we come for performing calculation. We can concatenate
# each character onto the new string and then convert the final string to an integer, we are
# initializing a string variable to hold the digit first or python will go error.
# By doing this we actually building up a number that's actually in a string and then converting that string back to an
# integer.
# number = "9,223,372,036,854,775,807"
# cleanedNumber = ' '
# for i in range(0, len(number)):
#     if number[i] in '0123456789':
#         cleanedNumber = cleanedNumber + number[i]
# newnumber = int(cleanedNumber)
# print("The number is {0} ".format(newnumber))

##################################

# for i in range(10):
#     print(i)

##################################

# by using char instead of len, it is going to do is extract a character that each position in that number string.

# number = "9,223,372,036,854,775,807"
# cleanedNumber = ''
#
# for char in number:
#     if char in '0123456789':
#         cleanedNumber = cleanedNumber + char
# Again, we're not having to use that number and the index position with the i anymore because we're actually using the
# for char directly.
# newNumber = int(cleanedNumber)
# print("The number is {}".format(newNumber))

# For loop assigns each character in the sequence number to a loop variable character as its going through each element
# in the actual string itself. so each time around the loop the variable char has the value of the next character from
# the string number

# for state in ["not pinin", "no more", "a staff", "bereft of life"]:
#     print("This parrot is " + state)
    # print("This parrot is {0}".format(state))

#  Each time it goes through the loop its going to actually add one of these to it automatically.
#  For loop range is just a tie, it just specifies the start and end, rather than listing all values.
#  In other words it's like a sequence of values, much like this, but instead of actually listing each and all of them.
#  We are just listing the start and then end.
#  range is start / stop and it can also include step. like below -

# for i in range(0, 100, 5):  # here 0 is starting and 100 is stopping but at te same time 5 is known as step i.e.
# dividable, which means printing all the number which is divisible by 5 in 0 to 100
#    print("i is {0}".format(i))  # which means jumping in loops

# nested loop in another loop is very much powerful way to use data

# Example:- How we can generate the times table used to teach children multiplication.

# for i in range(1, 21):
#     for j in range(1, 11):
#         print("{0} times {1} = {2}".format(i, j, i * j))
#     print("===================")  # Make sure print intend level is correct
#     print(' ')

##################################

# quote = """
# Alright, but apart from the Sanitation, the Medicine, Education, Wine,
# Public Order, Irrigation, Roads, the Fresh-Water System,
# and Public Health, what have the Romans ever done for us?
# """
# for char in quote:
#     if char in 'ABCDEFGHIJKLMNOPQRSTUVWHYZ':
#         # print(char, end=' ')
#         print(char, end=' ')

##################################
# Print all the numbers from 0 to 100 that are divisible by 7

for i in range(0, 101, 7):
    print(i)

# for i in range(101)[::7]:
#     print(i)











