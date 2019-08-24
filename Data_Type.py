a = 12
b = 3
print(a + b)
print(a - b)
print(a * b)
print(a / b)  # kindly mind to use / and //, look below for loop
print(a // b)
print(a % b)

for i in range(1, 4):
    print(i)

# for i in range(1, a/b):  # the reason for error is / it will give float number
#     print(i)

for i in range(1, a//b):  # this will not give error because o/p of a//b is integer number
    print(i)

print(a + b / 3 - 4 * 12)

# problem for this error is operator precedence which means all operator were given equal importance, so we would have
# got answer as 12 but the thing to remember is multiplication and division have
# higher operator precedence than addition and subtraction, so those are performed first.
# firstly b/3 = 1 then 4 times 12 = 48 is added, so actually (12 + 1 ) - 48 = -35.
# Because multiplication and division have higher operator precedence than addition and subtraction.
# One more thing it moves from left to right

print(8 / 2 * 3)  # Here Divide will perform first
print(8 * 3 / 2)  # Here Multiplication will be performed first

# To overcome from above issue, we can use parentheses to make it clear what we're trying to perform.

print((((a + b) / 3) - 4) * 12)

# To overcome of above complex statement we can avoid by using variable like below -

c = a + b
d = c / 3
e = d - 4
f = e * 12
print(f)

# Excercise -

bun_price = 2.40
money = 15
print(money // bun_price)

#########################

# String is called as Sequence Data Type which means sequence of character that you can put together that form a actual string

parrot = "Norwegian Blue"
print(parrot)

# Lets Play with String
print(parrot[0])
print(parrot[3])
# print(parrot[14]) # This will be out of range

# We can even count or go backward as well
print(parrot[-1])
print(parrot[0:6])  # This will get six characters starting at position zero and not including position 6.
print(parrot[:6])  # This will automatically start at zero position
print(parrot[6:])  # This will go till end and started at 6th position which means started at 7th position
print(parrot[-4:2])  # This will not print anything because you cant go back from the starting position
print(parrot[-4:-2])  # This will print because it started from the start of the string, its gone back four char, up to
                      # and inclusin the second to last char in the string which was the u
print(parrot[5:-7])  # -9 is making position from back and -7 is cutting that much position from back
print(parrot[-9:-7])  # Both will print same because in first we are moving from front and in second from back
print(parrot[5:7])  # This will also print the same, which means we can come with positive and negative both

# We can also use skip characters, counting in steps

print(parrot[0:6:2])  # Starting from index position zero, extract all the characters up to
                      # but not including index position Six  in steps of two, so it started on N
                      # and skip to r and skip to e ==> Norweg -- Nre
                      # Here 6 is making range then 0 is making starting point and 2 is making jump
                      # From  Norwegian Blue - 6 is making range so it is coming  Norweg and then
                      # Starting from 0 position so N printed and then 2 jump so 're' printed
                      # parrot[0:6:2] starts at position 0 and extend up to (but not including) position 6.
                      # It steps over the characters in 2s - so it skips every other character.

print(parrot[0:6:3])  # Similar logic applies here.

# We can skipp and jump as well

number = "9,223,372,026,453,112,124,567"
print(number[1::4])  # It skipped the number started as 1st position , then skipped 4 char because counter starts from 0

# number1 = "9,12,123,3456,7"
# print(number1[1:])

numbers = "1, 2, 3, 4, 5, 6, 7, 8, 9"
print(numbers[0::3])


days = "Mon, Tue, Wed, Thu, Fri, Sat, Sun"
print(days[::4])

string1 = "he's "
string2 = "probably "
print(string1 + string2)

print("hello " * 5)
print("hello " * (5+4))
print("hello " * 5 + "4")

today = "friday"
print("day" in today)
print("fri" in today)
print("thur" in today)
print("parrot" in "frt")

data = "1:A, 2:B, 3:C, 4:D, 5:E, 6:F, 7:G, 8:H"
print(data[::5])