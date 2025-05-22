# class contruction review


# defined the class

class Dog():
    # all attributes of the doggy class
    # methods and variables

    # init sets a universal variable that can be changed in further methods
    # init creates a universal variable of sorts
    # init doesn't need to take something in (other than self) but sometimes
    # you do want it to take in something
    # def __init__(self): is empty
    # name_input needs to be added to every time Dog is called/referenced
    def __init__(self, name_input):
        
        # "self" is here to set it in the namespace for an instance
        self.age = 0

        # assigning the dog's name to a class vairable
        self.name = name_input

    # all class methods must take "self" as the 0th input
    def bark(self):
        print("Woof woof!")

        # this calls the name specifically and will print Luna (in this ex)
        print(self.name + ", what do you see?")

    # method to age the dog ;-;
    # class methods always take in self at the 0th
    def birthday(self):

        # method to modify the age
        print("Happy birthday " + self.name + "!")
        self.age += 1
        if(self.age == 1):
            print(self.name + " is 1 year old!")
        else:
            print(self.name + " is " + str(self.age) + " years old!")
        return self.age

    def introduce(self):
        print("Hi, my name is " + self.name + " and I am "
              + str(self.age) + " years old!")
        

Luna_ = Dog("Luna")
# new instance of the dog class, saved under variable name Luna

# Luna_.bark()
# calls bark from the dog class, only because Luna now = dog

# self takes Luna as the 0th input over self, which "instance" of the class are
# we walking about

# accessing dog's age
Luna_.age

Luna_.introduce()

Luna_.bark()
Luna_.bark()

Luna_.birthday()

Luna_.birthday()

#look at the namespace for this particular dog and its age
