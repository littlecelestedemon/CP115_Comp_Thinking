# simple script to open a text file

file_name = "/Users/willapolman/Desktop/words.rtf"

# open returns a textiowrapper object
f = open(file_name)

# print what f is
# print(f)

# if you just print f, returns garbage

# to actually get into the file, need f.readline()
# get top line of file

line = f.readline()
print(line)

for i in range(8):
    line = f.readline().strip # end of line character
    print(line)

