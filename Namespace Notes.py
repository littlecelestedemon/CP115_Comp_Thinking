# global name space

x = 121

def fun():
    x = "catdog!"
    y = "pups"
    print(x)
    # this will print catdog even though x is already defined because it's inside
    # this namespace, not the global one
    
    # return y
    # also doesn't work because the function isn't being called AND it's still
    # only defined inside the temporary name space


fun()

print(x)

# print(y)
# will return a NameError because y isn't defined in the global space

