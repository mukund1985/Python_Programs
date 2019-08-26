# shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
# for item in shopping_list:
#     if item == "spam":
#         print("I am ignoring " + item)
#         # print("I am ignoring {0} ".format(item))
#         continue             # Continue Stop Processing any more lines in the block and forces the for loop to move on
# # to the next value in the sequence. Which means bypassed this.
#     print("Buy " + item)

# print('###############################')

# shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
# for item in shopping_list:
#     if item == "spam":
#         print("I am ignoring " + item)
#         # print("I am ignoring {0} ".format(item))
#         break             # Break - as soon as it hits match, it gets break.
#     print("Buy " + item)

###############################

# meal = ["egg", "bacon", "spam", "sausages"]
#
# nasty_food_item = ' '    # Initialization of variable
# for item in meal:
#     if item == 'spam':
#         nasty_food_item = item
#         break      # When we want to terminate the loop earlier, when early when some condition is met.
# else:
#     print(" I'll have a plate of that, then, please")
# if nasty_food_item == 'spam':
#     print("Can't I have anything without spam in it")

###############################

# Modify the code inside this loop to stop when i is exactly divisible by 11

for i in range(0, 100, 7):
    print(i)
    if i > 0 and i % 11 == 0:
        break



