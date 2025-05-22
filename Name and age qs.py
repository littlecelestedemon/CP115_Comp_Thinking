name = input("What is your name?")
age = input("How old are you?")

input("Is your name " + name + " and are you " + age + "? Answer with y or n")

if(input == "y"):
    print("Hello!")
else:
    print("I'm sorry, please type your name and age again")
    name = input("What is your name?")
    age = input("How old are you?")
    input("Is your name " + name + " and are you " + age + "? Answer with y or n")
