# review of if else statements
# to call an if statement:
# if booleanStatemenet == true:
#   block of code that follows if the condition is true
# else:
#   block of code that follows if the condition is false

# if elif else
#   elif gets used if there are more than two cases

userWord = input("What is your favorite color?")

def colorQuestion(userWord):

    if (userWord == "red" or userWord == "blue" or userWord == "purple"):
        return "I like that color"
    elif (userWord == "yellow" or userWord == "orange"):
        return "Those colors are so bright!"
    else:
        return "That's a fun color."

print (colorQuestion(userWord))

# elifs are important versus if if
# elif only happens if condition 1 is false and condition 2 is true
# if if happens if either are true
#   and else only happens if the last condition is false
