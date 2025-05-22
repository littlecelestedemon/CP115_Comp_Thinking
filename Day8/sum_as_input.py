
# method to apply a math function to everything in a list.
def apply_to_list(my_list, func):
    #empty list to hold results
    result_list = []

    #iterating over each entry in my_list
    for i in range(len(my_list)):
        # apply the function to the ith thing in the list,
        # and store the result. 
        result_list.append( func(my_list[i] )  )
    return result_list

# a simple math function
def power_of_2(x):
    return x * x

# another simple math function
def mult_by_2(x):
    return x * 2


target = [1,2,3,4,5,6,7]
print(target)
print( apply_to_list( target, mult_by_2  ) )
print( apply_to_list( target, power_of_2  ) )
