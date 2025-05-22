# Create a file named PopularName.py.
# This program will make use of the data in the us_names.zip file.
# When run from the same directory as the yob*.txt files,
#   the program will ask the user for starting and ending year as well
#   as the sex to scan.
# After receiving these three inputs, the program will find the most
#   popular name.
# "Popular" is defined as having been given the most times in the years
#   under consideration.


# recieve user inputs
yearBegin = input("Input a year to begin scan at: ")
yearEnd = input("Input a year to end scan at: ")
sexPref = input("Enter M, F or A for preferred sex: ")

# only used at the very end print statement
yearSet = yearBegin
yearEndSet = yearEnd

# prepare empty dictionary
names_All = {}

# loop through desired years
for year in range(int(yearBegin), int(yearEnd) + 1):

    # loop through lines in the file for one year
    filename = "/Users/willapolman/Downloads/us_names/yob"+str(year)+".txt"
    f = open(filename)
    line = f.readline()

    while (line):
        items = line.split(",")
        line_name = items[0]
        line_sex = items[1]
        line_uses = items[2]

        if (line_sex == sexPref or sexPref == "A"):
            if (line_name in names_All):
                names_All[line_name] = names_All[line_name] + int(line_uses)
            else:
                names_All[line_name] = int(line_uses)

        line = f.readline()

# empty to be filled popular stats
mostPopNum = 0
mostPopName = " "

# going through names in the dictionary for highest occurance
for name in names_All:
    times_used = names_All[name]

    # only checking for the highest value in the dictionary
    if (times_used > mostPopNum):
        mostPopNum = times_used
        mostPopName = name

print("The most popular name is " + \
      str(mostPopName) + " at " + \
      str(mostPopNum) + " uses between the years " + \
      str(yearSet) + " and " + str(yearEndSet) + ".")
