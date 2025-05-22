yearBegin = input("Input a year to begin scan at: ")
yearEnd = input("Input a year to end scan at: ")
sexPref = input("Enter M, F or A for preferred sex: ")

# only used at the very end print statement
yearSet = yearBegin
yearEndSet = yearEnd

# prepare empty dictionary
names_All = {}

# loop through desired years

# new filter code
def check_S(letter):
    if (letter == sexPref or sexPref == "A"):
        return True
    else:
        return False

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

        # only runs if the filter returns true, replaced an if-else statement
        if (filter(check_S, line_name)):
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
