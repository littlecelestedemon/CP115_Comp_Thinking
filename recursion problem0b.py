# 0b. write a recursive function which takes a list of numbers as input, and
#returns the minimum of that list.

theList = [1000000000]

def smallList():
    status = input("Give me a whole number. Type finished to stop.")
    if(status == "finished"):
        print(theList[int(0)])
        #only requests the first item in the list
    else:
        status = int(status)
        check = theList[int(0)]
        if(status < check):
        #only if the newest input is lower than a previous one will it be placed
        #in the list, otherwise ignored
           theList.insert(0, status)
        smallList()
    
smallList()

#side note, this took waaay longer than it should've because I didn't set
#status to an int, just had int(status)
