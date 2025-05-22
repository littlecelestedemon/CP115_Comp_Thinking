# The request "3d4" should roll a d4 three times and print the result.
# A valid result would be something like 3 1 4.

# Note that no dice have a zero spot! A d4 can be any of 1 to 4
# a d20 can be any of 1 to 20, etc.
# Your program should:
# import random
# use a while loop to continually ask the user for dice rolls until
# they say they are 'DONE'.
# For a given request XdY, print the result of rolling a dY die, X times.
# This means X many calls to randint(), with appropriate input parameters.
# Exit when the user is done.


# imports random class
import random

# *** this is new ***
class XdZero(Exception):
    pass
    # if the user inputted y as 0, error bc there's no such thing as a d0

class ZerodY(Exception):
    pass
    # if the user inputted x as 0, error bc you can't roll 0 times

# this specifically takes one input and splits it into two values
# with the "split" part of this code, it gets rid of "d" and assigns the first
# number to x and the second to y
# the only way I could think of? to take one input and make two values
x, y = input("Roll some dice in the format XdY! Type DONEdDONE when finished\n").split("d")

# input = "2d6"
# x = input[0]
# y = input[2]

# can also "step through" the "list" looking for "d" and assigning everything
# before "d" as x and everything after "d" as y

# for i in range(len(user_input)):
# if user_input[i] == "d"
# found_d = i
# x = user_input[:found_d]
# x = user_input[found_d+1:]

# unfortunate consequence is that this is messier and the exit requirement is weird

while (x != "DONE" or y != "DONE"):
    try:
        x = int(x)
        y = int(y)
        # might be unnecessary but pretty sure x and y need to be ints and were
        # strings from the input
        if (x != 0 and y != 0):
            # continues for the range x sets, how many times to "roll"
            for i in range(x):
                result = random.randint(1, y)
                # range of dice options are between 1 and y
                
                print (result)
            x, y = input("Roll some dice in the format XdY! Type DONEdDONE when finished\n").split("d")
        else:
            if (x == 0):
                raise ZerodY()
            if (y == 0):
                raise XdZero()
                        
    except ZerodY:
        print("You cannot roll 0 times! Try again.")
        x, y = input("Roll some dice in the format XdY! Type DONEdDONE when finished\n").split("d")
    except XdZero:
        print("You cannot roll a d0! Try again.")
        x, y = input("Roll some dice in the format XdY! Type DONEdDONE when finished\n").split("d")
    except:
        print("Uh oh, that input isn't accepted. Try again.")
        x, y = input("Roll some dice in the format XdY! Type DONEdDONE when finished\n").split("d")
