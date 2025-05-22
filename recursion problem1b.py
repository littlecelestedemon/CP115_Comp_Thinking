#1b, reverse 1a

theList = [1]

def askFor():
    status = input("Give me a whole number. Type finished to stop.")
    if(status == "finished"):
        del theList[len(theList)-1]
        #very similar to 1a, except it's removing the very last item which
        #would be the placeholder
        print(theList)
        return(theList)
    else:
        status = int(status)
        check = theList[0]
        #checks the earliest value
        check = int(check)
        if(status > check):
            theList.insert(0, status)
            #instead of putting it at the end, places it in front
        else:
            theList.insert(0, check)
        askFor()
askFor()
        
