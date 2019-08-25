#  For Loop:-  It actually takes a range of values and assign them one by one to a variable and then executes a block of
#  code once for each value.

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
number = "9,223,372,036,854,775,807"
cleanedNumber = ' '
for i in range(0, len(number)):
    if number[i] in '0123456789':
        cleanedNumber = cleanedNumber + number[i]
newnumber = int(cleanedNumber)
print("The number is {0} ".format(newnumber))

##################################

for i in range(10):
    print(i)
