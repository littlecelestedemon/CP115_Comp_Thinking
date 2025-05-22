# Problem 0.

# 0a) Write a recursive function which takes a list as input, and returns
# that list in reversed order.

# Example input: [0,1,67, 200, 4, 7, 'dog', 'cat']

# Example output: ['cat', 'dog', 7, 4, 200, 67, 1, 0]

# 0b) Write a recursive function which takes a list of numbers as input, and returns the minimum of that list.

# Example input: [0,1,67, 200, 4, 7,-20, -37, 23, 567]

# Example output: -37

status = input("Type things to put into a list! Type DONE when finished \n")
# userlist to be added to, otherwise returns blank
userList = []

# until status = DONE, loop will continue
while (status != "DONE"):
    userList.insert(0, status)
    status = input("Give a list of items seperated by spaces, type DONE when finished \n")

print(userList)
