x = 2

try:
    x = 1/0
except:
    pass

y = "dog"

# user input

# this will only turn true and continue if a can be converted into an int

# this is turned into a function/method so it can be called multiple times
def give_num():
    a_success = False

    a = input("Give me a number: ")

    while not a_success:
        try:
            a = int(a)
            a_success = True
        except:
            print("Gave me a bad input, try again.")
            a = input("Give me a number: ")

    return a

x = give_num()
y = give_num()

# defining own type of error
class TwoDivisionError(Exception):
    pass

# hasn't been defined yet, just that the thing exists. How? Python doesn't know

division_success = False

while not division_success:
    try:
        if y == 2:
            raise TwoDivisionError("We aren't allowed to divide by 2 either.")
        print(x/y)
        division_success = True

    except TwoDivisionError as e:
        print("I cannot divide by 2! Give me a new y.")
        y = give_num()
    except ZeroDivisionError as e:
        print(e)
        print("I can't divide by 0! Give me a new y.")
        y = give_num()

            
