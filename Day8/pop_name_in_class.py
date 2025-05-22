# Task 1: getting a range of years and assigned sex from the user.
start = input("Give me a starting year.")
end = input("Give me a ending year.")
a_sex = input("M/F/A?")

# Task 2: looping through all of the years in that range.
for year in range(int(start), int(end)+1):
    print(year)

# Task 3: looping through all of the lines in the file for one year.
filename = "/home/cory/CC21-22/Teaching/BA - CP115/ClassMaterials/Day7/us_names/yob"+year+".txt"

f = open(filename)
line = f.readline()
while line:
    items = line.split(',')
    line_name = items[0]
    line_sex = items[1]
    line_uses = items[2]
    line = f.readline()
    
# Task 4: adding together how many times we've seen each name.


# Task 5: printing which name has the most uses








"""
# Task 1: get a year from the user.
year = input("What year would you like to search?")
# Task 2: get a name from the user.
name = input("What name would you like to search for?")

print(year, name)


# Task 3: open the file associated with that year.
filename = "/home/cory/CC21-22/Teaching/BA - CP115/ClassMaterials/Day7/us_names/yob"+year+".txt"

f = open(filename)

# Task 4: see how many times the name was used in the year. 

line = f.readline()
while line:
    items = line.split(',')
    line_name = items[0]
    line_sex = items[1]
    line_uses = items[2]
    if name == line_name:
        print( "The name " + name + " was used " + line_uses + " in the year " + \
               year + ", associated with assigned sex " + line_sex + ".")

    line = f.readline()
"""
