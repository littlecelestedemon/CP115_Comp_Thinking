# Task 1: getting a range of years and assigned sex from the user.
start = input("Give me a starting year.")
end = input("Give me a ending year.")
a_sex = input("M/F/A?")

name_use_db = {"Emma":0, "Alex":0}

name_use_db["David"] = 0

# Task 2: looping through all of the years in that range.
for year in range(int(start), int(end)+1):
    print(year)

    # Task 3: looping through all of the lines in the file for one year.
    filename = "/home/cory/CC21-22/Teaching/BA - CP115/ClassMaterials/Day7/us_names/yob"+str(year)+".txt"

    f = open(filename)
    line = f.readline()
    while line:
        items = line.split(',')
        line_name = items[0]
        line_sex = items[1]
        line_uses = items[2]
        if line_sex == a_sex or a_sex == 'A':
            if line_name in name_use_db:
                name_use_db[line_name] = name_use_db[line_name] + int(line_uses)
            else:
                name_use_db[line_name] = int(line_uses)
        line = f.readline()

max_seen_so_far = 0
best_name_so_far = "Cory"

for name in name_use_db:
    times_used = name_use_db[name]
    if times_used > max_seen_so_far:
        max_seen_so_far = times_used
        best_name_so_far = name

print("The name " + best_name_so_far + \
      " was used " + str(max_seen_so_far) + " times in that range.")

#print("The name Emma was used " + str(name_use_db["Emma"]) + " times in that range.")
#print("The name Alex was used " + str(name_use_db["Alex"]) + " times in that range.")

#print(name_use_db)    
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
