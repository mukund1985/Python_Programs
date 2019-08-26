# Create a program that takes an IP address entered at the keyboard and prints out the number of segments it contains,
# and the length of each segment.

# An ip address consists of 4 numbers, separated from from each other with a full stop. But your program should just
# count however many are entered.

ipAddress = input("Please enter an IP address: ")

segment = 1  # Initializing variables
segment_length = 0

# Each time when we find a full stop or period in the input string we're going to increment a counter of how many
# segments there are, now unless the input is blank they'll always be at least one segment, we're going to initialize
# the variable segment to a one >> segment = 1
# Now we will also count how many character are in each segment so the variable-length will be used for that.

# Now the next step will be now is to loop through all the characters in the input string IP address and check to see if
# you've got a full stop or some other character. Below is the code for that -

for character in ipAddress:  # looping through all the characters in the input string IP address
    if character == '.':
        print("segment {} contains {} characters ".format(segment, segment_length))
        segment += 1
        segment_length = 0
    else:
        segment_length += 1
# Ri



