# Problem 0.

# 0a) Write an iterative program which takes a list as input, and returns
# that list in reversed order.
# Example input: [0,1,67, 200, 4, 7, 'dog', 'cat']
# Example output: ['cat', 'dog', 7, 4, 200, 67, 1, 0]

# pre-set list
setList = [0,1,67, 200, 4, 7, "dog", "cat"]

# empty list to add things to
reversedList = []

# will continue until setList is completely empty
# for loop would also work, however, I was thinking user input was required so
# oops
while (len(setList) != 0):

    # inserts into the 0th spot the setList's 0th item
    reversedList.insert(0, setList[0])
    print (setList)

    # removes the item in the 0th spot in setList
    del setList[:1]

print(reversedList)
