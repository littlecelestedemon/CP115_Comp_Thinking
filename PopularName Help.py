# Create a file named PopularName.py.
# This program will make use of the data in the us_names.zip file.
# When run from the same directory as the yob*.txt files,
#   the program will ask the user for starting and ending year as well
#   as the sex to scan.
# After receiving these three inputs, the program will find the most
#   popular name.
# "Popular" is defined as having been given the most times in the years
#   under consideration.

# 1 Take 3 inputs, two years and a sex (or A)
# 2 have those down, just don't have counting up the names
# 3 loop over years, loop over lines of files with each year
# 4 adding together how many times we've seen each name
# * task 4 stumped me
# 5 print the name which has the most uses

name_Dictionary = {"Willa" : 0}
biggestNum = 0
biggestName = " "

 #name_Dictionary[line_name] = int(line_uses)

start_year = input("Give me a starting year: ")
end_year = input("Give me a ending year: ")
sex_pref = input("M/F/A?")

# loops over years
for i in range(int(start_year), int(end_year) + 1):
    
    filename = "/Users/willapolman/Downloads/us_names/yob"+str(i)+".txt"

    f = open(filename)
    line = f.readline()

    # loops over names
    while (line):
        items = line.split(",")
        line_name = items[0]
        line_sex = items[1]
        line_uses = items[2]

        line_uses = int(line_uses)

        # checks to see if the current name adheres to sex specified
        if (sex_pref == line_sex or sex_pref == "A"):

            # if the current name is already in the dictionary, add up
            if (line_name in name_Dictionary):
                name_Dictionary[line_name] = name_Dictionary[line_name] + int(line_uses)
            else:
                # if the name isn't in the dictionary, add it with the current val
                name_Dictionary[line_name] = int(line_uses)
            
        line = f.readline()

for items in name_Dictionary:
    times_used = name_Dictionary[name]
    if times_used > biggestNum:
        biggestNum = times_used
        biggestName = name
        
print(biggestName)
print(biggestNum)
    
# name that's used to most times

# gets the numbers for set names like my name
print("Willa was used " + str(name_Dictionary["Willa"]) + " times.")
