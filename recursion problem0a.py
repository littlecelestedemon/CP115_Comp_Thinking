#0a problem: Write a recursive function which takes a list as input, and
#returns that list in reversed order.

theList = []

def askFor():
    status = input("Give me something to put into the list. Type finished to stop.")
#taking the input/what's to be put in the list
    if(status == "finished"):
#only ends if this is printed
        print(theList)
        return(theList)
    else:
        theList.insert(0, status)
        askFor()
#automatically puts it in one after the other and repeats the function
askFor()
            
