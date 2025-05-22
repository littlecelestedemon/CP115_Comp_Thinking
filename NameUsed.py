# Create a file named NameUsed.py.
# This program will make use of the data in the us_names.zip file.
# When run from the same directory as the yob*.txt files, the program will
#   ask the user for a name and year.
# The program will then search in the file for that year and print
#   a message indicating whether the name was in the data set for that year
#   and which sexes the name was associated with.

# gets the year and name desired
year = input("Input a year: ")
name = input("Search for a name in that year: ")

# finds the file, all in the same location w dif names for the year
filename = "/Users/willapolman/Downloads/us_names/yob"+year+".txt"

# requests to open the file
f = open(filename)

# requests to look at the first line
line = f.readline()

# this is used to check if the name was found at all in the process
found_name = "null"

while (line):
    # removes the , in the line
    items = line.split(",")
        
    line_name = items[0]
    line_sex = items[1]
    line_uses = items[2]
    if (name == line_name):
        # if the name is found, this triggers
        found_name = name
        print ("The name " + name + " was used " + \
                line_uses + " times in the year " + \
                year + " with associated sex " + line_sex + ".")
            
    line = f.readline()

# only if the program did not find the name once will this run
if (name != found_name):
    print ("The name " + name + " was not used in the year " + year + ".")
