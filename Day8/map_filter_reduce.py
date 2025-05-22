from functools import reduce

# Example of filter
names = ["Emma", "Egbert", "David", "Charmander", "Geoff"]

def check_E(string):
    if string[0] == "E":
        return True
    else:
        return False

print( list( filter(check_E, names)))

# Example of reduce

def my_mult(x, y):
    return x * y

print( reduce(my_mult, [1,2,3,4,5]) )
