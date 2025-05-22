#0a problem: Write a recursive function which takes a list as input, and
#returns that list in reversed order.

def reverseList(theList):
    if len(theList) <= 1:
        #if the list is empty or just has one number, returns without recursion
        return(theList)
    else:
        elZero = theList[0]
        # takes the "first element"
        newList = theList[1:]
        # new list is everything but the first element
        restOfList = reverseList(newList)
        # recursion
        finalList = restOfList + [elZero]
        return finalList

userList = input("Give a list of ints seperated by spaces")
input_list = userList.split(" ")

print(reverseList(input_list))
#takes a user list as strings

# print(reverseList([1, 2, 3, 4, 5, 6]))
