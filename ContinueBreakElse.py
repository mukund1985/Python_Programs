shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
for item in shopping_list:
    if item == "spam":
        continue             # Continue Stop Processing any more lines in the block and forces the for loop to move on
# to the next value in the sequence.
    print("Buy " + item)