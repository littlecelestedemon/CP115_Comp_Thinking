#1a, The "cumulative max" or cmax is an operation we can apply to a list.
#It means the max of the list up to a given entry.
#The left-hand cumulative max is a new list where the ith entry is the max
#of entries 0 through i-1.
#The right-hand cumulative max is a new list where the ith entry is the max of
#entries i though the end.

theList = [1]

def askFor():
    status = input("Give me a whole number. Type finished to stop.")
    if(status == "finished"):
        del theList[0]
        #disliked the empty list so the 1 is a placeholder that's removed before
        #the list is returned
        print(theList)
        return(theList)
    else:
        status = int(status)
        check = theList[len(theList)-1]
        #needs to check the item that's last in the list's value
        check = int(check)
        if(status > check):
            theList.append(status)
        else:
            theList.append(check)
        askFor()
askFor()
        
