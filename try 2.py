import functools

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

# You must use the method reduce in your solution.
# Demonstrate that your function works on sum, max and min,
#   which are all built into Python.

def sequence_examiner(the_list, num, function):
    results = []

    for i in range(num):
        results.append(functools.reduce(function,the_list))
        
    return results

set_list = [0,1,1,2,3,5,8,13,21,34]

print(sequence_examiner(set_list, 5, sum))

