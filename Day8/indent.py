# how indentation separates blocks of code in Python.
import random

choice = input("Heads or Tails")
coin_flip = random.randint(0,1)

if (coin_flip == 0 and choice == "Heads") or (coin_flip == 1 and choice == "Tails"):
    print("You win!")
    print("Darn.")
    print("You always beat me.")
    print(":(")
    if choice == "Tails":
        print("Ok! I'll choose tails next time")
    else:
        print("Dibs on choosing Heads")
    #
    #
    #
    #
    #
else:
    print("Hahah! I win")

num_lines = 0

while num_lines < 10:
    print("I'm the best at Heads and Tails")
    print("ha ha ha")
    num_lines = num_lines + 1

print("woo hoo!")



    
