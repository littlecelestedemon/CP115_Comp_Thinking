#I figured else-if statements existed in Python because of my experience
#with other languages

#Day is takes the input from the user and turns it into a variable to compare
#to the if else loop to determine outcome
#First checks if the input matches the strings Saturday or Sunday
#If it doesn't it then checks for Monday, and if it fails that, it checks for
#the other days
#If it isn't any of the other listed days, then it spits out Sorry and stops

print("Write dayMsg() to start this program")

def dayMsg():

    day = input("Day name (Tuesday, Monday, etc.):")

    if (day=="Saturday" or day=="Sunday"):
        print("Yay! It's the weekend!")
    elif (day=="Monday"):
        print("Yay! I've got the Mondays!")
    elif (day=="Tuesday" or day=="Wednesday" or day=="Thursday" or day=="Friday"):
        print("...just a regular day...")
    else:
        print("Sorry... I don't know that day.")

dayMsg()
