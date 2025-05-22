from functools import reduce

# ex of filter

names = ["Bulbasaur", "Charmander", "Squirtle", "Snorlax", "Swinub", "Articuno"]

def check_S(string):
    if string[0] == "S":
        return True
    else:
        return False


# have to force to return as a list, not just the thing
print(list(filter(check_S, names)))

# ex of reduce

def my_mult(x, y):
    return x * y

print(reduce(my_mult, [1, 2, 3, 4, 5]))
