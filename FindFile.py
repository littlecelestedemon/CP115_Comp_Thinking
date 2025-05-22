# homework tonight may be rough
# Task 1: get a year from user
#   Ask for an input, set it to year
# Task 2: get a name from user
#   Ask for a name
# Task 3: open file associated with that year
#   need help with that
# Task 4: see how many times the name was used in the year
#   have to split the comma character to get the seperate numbers for how many
#   times

filename = "can't find is :("

# careful about male and female for a name, give an associated gender

f = open(filename)

line = f.readline()

while line:
    items = line.split(",")
    line_name = items [0]
    line_sex = items [1]
    line_uses = items [2]
    if name == line_name:
        print ("The name " + name + " was used " + \
               line_uses + " in the year " + year + ".")

        line = f.readline()
