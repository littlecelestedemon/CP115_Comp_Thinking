# 0b) Write an iterative program which takes a list of numbers as input
# and returns the minimum of that list.

# Example input: [0,1,67, 200, 4, 7,-20, -37, 23, 567]
# Example output: -37

setList = [0,1,67, 200, 4, 7,-20, -37, 23, 567]

# runs for as many items exist in the list
for i in range(len(setList)):

    # first if statement exists only for the first "run" because there'd be
    # nothing to compare it to and that'd persumably be a problem
    if (i == 0):
        smallest = setList[0]
    else:
        
        # only if the next item is smaller than the current smallest will this
        # happen
        if (smallest > setList[i]):
            smallest = setList[i]

print (smallest)
