#  For Loop:-  It actually takes a range of values and assign them one by one to a variable and then executes a block of
#  code once for each value.

#  We will be printing at the values from 1 to 20

for i in range(1, 20):
    print(" i is now {0}".format(i))

number = "9,223,372,036,854,775,807"
for i in range(0, len(number)):  # Function len is an abbreviation for length and returns the length of a string
    print(number[i])
