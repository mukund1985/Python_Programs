age = 24
month = 2
day = 23
print("My Age is " + str(age) + " Years")  # str will converting what's in the bracket to string

# To come out of above conversion python gives replacement feilds and this is gonna be a
# a way that makes it a lot easier to make changes like this, when your dealing with multiple
# numbers on the one line.

print("My age is {0} Years , {1} Month and {2} Day ".format(age, month, day))

# This above is called a replacement field and this is the actual replacement for this part here.
# It is useful when we have lots of data.

print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7} ".format(31, "January",
                                                                           "March", "May", "July", "August", "October",
                                                                           "December"))

print(""" January: {2}
February: {0}
March: {2}
April: {1}
May: {2}
June: {1}
July: {2}
August: {2}
September: {1}
October: {2}
November: {1}
December: {2}""".format(28, 30, 31))

print("My age is %d years" % age)  # Old format

print(
    "My age is %d %s , %d %s " % (age, "Years", month, "Month"))  # %d is for integer and %s is for string %f for float

for i in range(1, 12):
    print("No. %2d squared is %4d and cubed is %4d" % (i, i ** 2, i ** 3))  # ** is work as squar root

print("Pi is approximately %12.50f" % (22 / 7))

for i in range(1, 12):
    print("No. {0:2} squared is {1:<4} and cubed is {2:<4}".format(i, i ** 2, i ** 3))  # This is the new python 3 for
    # {0:2} == First field is replacement for you number and that's which value from the area after the .format is
    # actually used in which spot. So colon two meant we allocated a width of 2 and colon 4 we allocated a width of four

print("Pi is approximately {0:12.50}".format(22 / 7))

for i in range(1, 12):
    print("No. {} squared is {} and cubed is {:4}".format(i, i ** 2, i ** 3))  # This will also take the 1st and
                                                                               # 2nd position automatically.
