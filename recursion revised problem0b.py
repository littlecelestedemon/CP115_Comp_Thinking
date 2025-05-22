# 0b. write a recursive function which takes a list of numbers as input, and
#returns the minimum of that list.

smallestList = [100000000]

def minList(theList):
    if len(theList) <= 1:
        initial = smallestList[0]
        second = theList[0]
        initial = int(initial)
        second = int(second)
        #smallest cannot be empty
        #conflict came when trying a single list
        if initial > second:
            smallest = theList[0]
            #if the only thing left in the list is bigger than 10000000 etc
            #accounts for lists with one item initially
        else:
            smallest = smallestList[0]
            #accounts for lists with more than one item
        #if the list is empty or just has one number, returns without recursion
        #smallestList seemingly has to not be empty, 1 is placeholder
        print (smallest)
        return smallest
    else:
        elZero = theList[0]
        elZero = int(elZero)
        #takes the first element of the list and compares to the current small
        newList = theList[1:]
        current_small = smallestList[0]
        if elZero < current_small:
            #only if the new element is smaller than the current will this occur
            current_small = elZero
            smallestList.insert(0, current_small)
            minList(newList)
            return newList
        else:
            minList(newList)
            return newList
        #retries with a new list with one less element

userList = input("Give a list of ints seperated by spaces")
input_list = userList.split(" ")

minList(input_list)

#has to not be a print statement here because it will print the remaining list

#takes a user list as strings

# print(reverseList([1, 2, 3, 4, 5, 6]))
