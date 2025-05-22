# will print the range of 5-10 as a list
print(list(range(5,10)))

for iteration in range(10):
    print(iteration)
    # prints out all of the things in the range


print("***")

my_list = ["lovely", "duck", 10, True]

# prints out all the individual items in a list seperately
for i in range(len(my_list)):
    print (i)
    print (my_list[i])

# can also use for element in my_list: print (element) but is not the pref

print("***")

# while looooop

status = input("Enter an int or write DONE \n")
#\n is just for aesthetic reasons

result = 1

while (status != "DONE"):
    # turning the status into an integer so it can be multiplied by the
    # initial 1
    result = result * int(status)
    
    # needs to re-ask 
    status = input("Enter an int or write DONE \n")

print(result)
# will only print the final result
# also I guess in the global namespace so result can be called
