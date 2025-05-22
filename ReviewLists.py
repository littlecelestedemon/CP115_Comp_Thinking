# making a list into a dictionary
# list can be empty or full

listName = []

# listName.append(variable) adds something to the end of the list
# listName.insert(0, variable) inserts the variable to the location of the list
# del listName[0] removes the item in the location
# can get things out of the list by calling the item in the location
# -1 indicates the last item in the list, and - says count back from the end
# can also slice a list with [:1] and [1:]
# first indicates everything up to but not including the last number
# second indicates everything including the first number

listName.append("dog")

print (listName)

listName.append("cat")

print (listName)

del listName[0]

print (listName)

listName.insert(0, "horse")

print (listName)

listName.append("parrot")

print (listName)

listName.append("snake")

print (listName)

print (len(listName))

print (listName[-2])

print ("**********")

# dictionary is similar to a list that instead make pairs of items associated
#   with each other
# one way of making a dictionary:

theDictionary = {"Key" : "Value", "Luna" : "Dog", "Chloe" : "Cat"}

# keys and values can be any noun (string, int, etc, can't be a list) in python
# keys cannot be the same but values can be
# use the keys to look up values like a human dictionary

# another way of making a dictionary:

theBlankDictionary = {}

theBlankDictionary["Goldie"] = "Goldfish"

# get things out of the dictionary by using keys, cannot use values

print(theDictionary ["Luna"])
print(theBlankDictionary["Goldie"])

# [] around key because it's basically indexing into a dictionary
