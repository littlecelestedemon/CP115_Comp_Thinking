# takes and looks at a number of eggs in a carton

class EggCarton:

    #defines the initial eggs list
    def __init__(self):
        self.eggs_Initial = 12

    #takes one egg from the initial eggs
    def take(self):
        #only if the universal egg count is higher than 1 will an egg be removed
        if self.eggs_Initial > 0:
            print("Took an egg from carton")
            self.eggs_Initial = self.eggs_Initial - 1
            return True
        else:
            #will only print this after egg count is 0
            print("Carton is now empty")
            return False

    #checks how many eggs are in the carton
    def look(self):
        return self.eggs_Initial

def empty(cart):
        if (cart.take()):
            print(".")
            empty(cart)
        else:
            # All out of eggs
            print("The carton is now empty")


cart1 = EggCarton()
cart2 = EggCarton()

# carton 1
print("Carton 1 contains " + str(cart1.look()) + " eggs")
print("taking 3 eggs")
cart1.take()
cart1.take()
cart1.take()
print("Carton 1 contains " + str(cart1.look()) + " eggs")

# carton 2
print("Carton 2 contains " + str(cart2.look()) + " eggs")
empty(cart2)
print("Carton 2 contains " + str(cart2.look()) + " eggs")
