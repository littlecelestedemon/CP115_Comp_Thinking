# I seem to need fibonacci as a function,
#   so here's a pretty messy one that works

def fibonacci(n):
    result = []
    num = 0

    # runs for as long as the number is set
    for i in range(n):
        if (i == 0):
            result.insert(0, i)
            # for the first time, it'll always be 0
            
        elif (i == 1):
            result.insert(1, i)
            # for the second time, it'll always be 1
        else:
            result.append(result[i-1] + result[i-2])
            # needs above because otherwise the request is outside of the index

    # returns a list
    return result

# returns an int

# 0a) We have seen several examples of recursively defined functions,
#   like the Fibonacci sequence and the Collatz sequence.
# Write a method sequence_examiner.
# Sequence examiner takes three arguments:
#   1) a sequence function like Collatz or Fibonacci.
#   2) A number n.
#   3) a function we want to compute over the whole list.

# For example, say we have a function fibbonaci(n) which computes the nth
#   Fibonacci number.
# sequence_examiner(fibonacci, 10, max) would compute the maximum of the
#   first 10 Fibonacci numbers.

# You must use the method map in your solution.
# Demonstrate that your function works on sum, max and min,
#   which are all built into Python.

def addition(n):
    return n + n

def squared_by_2(n):
    return n * n

def sequence_examiner(the_list, num, function):
    return map(function, the_list)

set_list = [1,2,3,4,5]
print(list(sequence_examiner(set_list, 1, max)))

# 0b) Write a method avg which returns the average of a list of numbers.
# The average of a collection of numbers is defined as the sum of the list
#   divided by the length of the list.
# Use this function, as well a sequence_examiner, to get the average of
#   the first 1 Fibonacci numbers, first 2 Fibonacci numbers, first 3 ...
#   first 100 Fibonacci numbers.
# Are these averages doing anything interesting?

"""

def avg(my_list):
    total = 0
    for i in range(len(my_list)):
        total += my_list[i]
        print (total)

    total = total / len(my_list)

    return total

print (avg([1,2,3,4,5]))

"""
