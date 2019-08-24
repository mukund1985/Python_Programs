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

number = "9,223,372,036,854,775,807"
for i in range(0, len(number)):
    if number[i] in '0123456789':
        print(number[i])
