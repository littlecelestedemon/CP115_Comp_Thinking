# recursion review

# reverse a list using recursion
# recursion's just about three things really
# - what's the simplest version of the problem?
# - how do we split up a problem into multiple smaller problems that
#   can be tackled in the same way?
# - if we have the solutions to the smaller problems, how do we combine them
#   into a solution to the original problem?

# defining a method for reversing a list:

def reverse(setList):
    #simplest version of the problem: if the list has 0 or 1 item
    if (len(setList) <= 1 ):
        #less than or equal to 1
        return setList
    #otherwise, need to continue
    else:
        # can break the problem into two questions:
        # a) breaking apart the list, and reversing each part
        zeroth_Element = setList[0]
        restof_List = setList[1:]
        
        print (restof_List)
        print (zeroth_Element)

        #recursion here uwu
        #also reverse_Rest is keeping track of all the stuff being reversed
        reverse_Rest = reverse(restof_List)
        
        # b) combining the reversed parts

        return reverse_Rest + [zeroth_Element]

print (reverse([]))
print ("***")
print (reverse([10]))
print ("***")
print (reverse([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))

# at the first level of recursion, 10 gets split off and calls [9, ... 1]
# then the second level of recursion, 9 gets split off and calls [8, ... 1]
# etc etc
