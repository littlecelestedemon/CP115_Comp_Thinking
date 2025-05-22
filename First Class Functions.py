# method to apply a math function to everything in a list

def apply_to_list(my_list, func):
    # empty to hold results
    results_list = []

    # iterating over each entry in the list
    for i in range(len(my_list)):
        # apply the function to the ith thing in the list
        # store result
        results_list.append(func(my_list[i]))

    return results_list

# simple maths

def power_of_2(x):
    return x * x

def multiply_by_2(x):
    return x * 2

target = [1,2,3,4,5,6,7]

print(target)
print(apply_to_list(target, multiply_by_2))

# so what this is saying is the call upon apply to list with target (list) and
# another function as the fun

# this will multiply everything in the list by 2 because of the mult by 2

print(apply_to_list(target, power_of_2))
