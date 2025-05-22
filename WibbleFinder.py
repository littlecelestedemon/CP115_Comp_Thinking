# Problem 0
# Previously, we learned Python's standard pattern for reading text files,
#   as well as ways to take in input from the command line.
# We also know how to find matching strings within a line of text.
# Write a program called WibbleFinder.py that:

# 1) takes in the name of a text file from the command line;
# 2) reads that file;
# 3) counts how many occurrences of the substring "wibble" occur in the file;
# 4) prints the average number of wibbles per line.
# Your program should gracefully handle the cases where a)
#   the user gives a file name that is not a valid file, or b) the file has zero lines.
# You can try your program out on the included files puck.txt
# Download puck.txt and an empty file (that you create) named empty_puck.txt.

class emptyFile(Exception):
    pass

name = input("Give me the name of a text file: ")

# can only call files in this specific location
filename = "/Users/willapolman/Downloads/us_names/"+name+".txt"

# if this all goes well, fine and good, otherwise...
try:
    f = open(filename)
    line = f.readline()

    countWibble = 0
    countLineNums = 0

    # this checks if the first line is empty
    if (len(line.strip()) == 0 and countLineNums == 0):
        raise emptyFile()

    string = "wibble"

    while (line):
        # if the string "wibble" is found, the wibble counter goes up
        if (string in line):
            countWibble += 1

        # always goes up regardless of wibble status
        countLineNums += 1
        line = f.readline()

    print(str(countWibble) + " wibbles found.")
    print("Average of " + str(countWibble/countLineNums) + " wibbles per line.")

# if the emptyFile flag is raised
except emptyFile:
    print("There is nothing in this file...")

# if it fails out but the emptyFile flag isn't raised
except:
    print("Something went wrong, I don't think that's a file avaliable.")
