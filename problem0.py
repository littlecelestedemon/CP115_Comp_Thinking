# 0a) Write three functions f, g, and h.
# Each of these should be mathematical functions that take one input, and
#   return one output, like the examples we used in class.
# Note, you may not use the same functions we used in class. 

# divide by 2
def f(x):
    return x / 2

# finds the nth object of the fibonacci sequence
def g(x):
    return x * 2 - 20

"""

    result = []
    num = 0

    # runs for as long as the number is set
    for i in range(x):
        if (i == 0):
            result.insert(0, i)
            # for the first time, it'll always be 0
            
        elif (i == 1):
            result.insert(1, i)
            # for the second time, it'll always be 1
        else:
            result.append(result[i-1] + result[i-2])
            # needs above because otherwise the request is outside of index

    # returns an int
    return result[len(result)]

"""

# essentially multiply by 2
def h(x):
    return x + x


# 0b) Demonstrate that you can use map to apply each of these functions
# to range(100), and print the results.

print("*** 0b below ***")

# range of 100 to be run through the functions
f_mapped = list(map(f, range(100)))
g_mapped = list(map(g, range(100)))
h_mapped = list(map(h, range(100)))

print(f_mapped)
print(g_mapped)
print(h_mapped)


# 0c) Demonstrate that you can use reduce, along with the functions you defined in part 0a,
#   to get the max of each function on range(100).

from functools import reduce

print("*** 0c below ***")

f_max = reduce(max, f_mapped)
g_max = reduce(max, g_mapped)
h_max = reduce(max, h_mapped)

print(f_max)
print(g_max)
print(h_max)


# 0d) Write a method function_examiner.
# function_examiner should take the following as inputs:

# a list of math functions
# a list of numbers
# a list of summarizers.
#   Summarizers are functions which take in a sequence and output a single
#   number that summarizes that sequence - like min, max, or sum.
#   note: this isn't an official Python term or anything!

# This method should print a table where each entry is the result of applying
#   a function to our list of numbers, and then summarizing the sequence
#   that results.

print("*** 0d below ***")

"""

def function_examiner(math_func, a_list, single_int_func):
    result = ""
    result1 = ""
    result2 = ""

    # checking the length of single_int_func to account for a list
    for i in range(len(single_int_func)):
        if i == 0:
            if single_int_func[0] == max:
                result = "max"
            if single_int_func[0] == min:
                result = "min"
            if single_int_func[0] == sum:
                result = "sum"
        elif i == 1:
            if single_int_func[1] == max:
                result1 = "max"
            if single_int_func[1] == min:
                result1 = "min"
            if single_int_func[1] == sum:
                result1 = "sum"
        elif i == 2:
            if single_int_func[2] == max:
                result2 = "max"
            if single_int_func[2] == min:
                result2 = "min"
            if single_int_func[2] == sum:
                result2 = "sum"

    # finding which math function is where
    func = ""
    func1 = ""
    func2 = ""
    for j in range(len(math_func)):
        if j == 0:
            if math_func[0] == f:
                func = "f"
            if math_func[0] == g:
                func = "g"
            if math_func[0] == h:
                func = "h"
        elif j == 1:
            if math_func[1] == f:
                func1 = "f"
            if math_func[1] == g:
                func1 = "g"
            if math_func[1] == h:
                func1 = "h"
        elif j == 2:
            if math_func[2] == f:
                func2 = "f"
            if math_func[2] == g:
                func2 = "g"
            if math_func[2] == h:
                func2 = "h"
                
    # putting it together
    if len(math_func) == 2:
        fin = result+"("+func+"("+str(a_list[0])+"), "+func+"("+str(a_list[1])+"), "+func+"("+str(a_list[2])+"), "+func+"("+str(a_list[3])+"))"
        fin1 = result+"("+func1+"("+str(a_list[0])+"), "+func1+"("+str(a_list[1])+"), "+func1+"("+str(a_list[2])+"), "+func1+"("+str(a_list[3])+"))"
        
        fin2 = result+"("+func+"("+str(a_list[0])+"), "+func+"("+str(a_list[1])+"), "+func+"("+str(a_list[2])+"), "+func+"("+str(a_list[3])+"))"
        fin3 = result1+"("+func1+"("+str(a_list[0])+"), "+func1+"("+str(a_list[1])+"), "+func1+"("+str(a_list[2])+"), "+func1+"("+str(a_list[3])+"))"
        print (fin + " " + fin2)
        print (fin2 + " " + fin3)
        print("")


    if len(math_func) == 3 and len(a_list) < 10:
        # extremely long variables that prints out the desired result
        # sans table
        fin = result+"("+func+"("+str(a_list[0])+"), "+func+"("+str(a_list[1])+"), "+func+"("+str(a_list[2])+"), "+func+"("+str(a_list[3])+"), "+func+"("+str(a_list[4])+"))"
        fin1 = result+"("+func1+"("+str(a_list[0])+"), "+func1+"("+str(a_list[1])+"), "+func1+"("+str(a_list[2])+"), "+func1+"("+str(a_list[3])+"), "+func1+"("+str(a_list[4])+"))"
        fin2 = result+"("+func2+"("+str(a_list[0])+"), "+func2+"("+str(a_list[1])+"), "+func2+"("+str(a_list[2])+"), "+func2+"("+str(a_list[3])+"), "+func2+"("+str(a_list[4])+"))"

        fin3 = result1+"("+func+"("+str(a_list[0])+"), "+func+"("+str(a_list[1])+"), "+func+"("+str(a_list[2])+"), "+func+"("+str(a_list[3])+"), "+func+"("+str(a_list[4])+"))"
        fin4 = result1+"("+func1+"("+str(a_list[0])+"), "+func1+"("+str(a_list[1])+"), "+func1+"("+str(a_list[2])+"), "+func1+"("+str(a_list[3])+"), "+func1+"("+str(a_list[4])+"))"
        fin5 = result1+"("+func2+"("+str(a_list[0])+"), "+func2+"("+str(a_list[1])+"), "+func2+"("+str(a_list[2])+"), "+func2+"("+str(a_list[3])+"), "+func2+"("+str(a_list[4])+"))"                                                                                                                                                           

        fin6 = result2+"("+func+"("+str(a_list[0])+"), "+func+"("+str(a_list[1])+"), "+func+"("+str(a_list[2])+"), "+func+"("+str(a_list[3])+"), "+func+"("+str(a_list[4])+"))"
        fin7 = result2+"("+func1+"("+str(a_list[0])+"), "+func1+"("+str(a_list[1])+"), "+func1+"("+str(a_list[2])+"), "+func1+"("+str(a_list[3])+"), "+func1+"("+str(a_list[4])+"))"
        fin8 = result2+"("+func2+"("+str(a_list[0])+"), "+func2+"("+str(a_list[1])+"), "+func2+"("+str(a_list[2])+"), "+func2+"("+str(a_list[3])+"), "+func2+"("+str(a_list[4])+"))"

        # possibly the ugliest piece of code I've written
                                                                                
        print (fin)
        print(fin1)
        print(fin2)
        print("")
        print(fin3)
        print(fin4)
        print(fin5)
        print("")
        print(fin6)
        print(fin7)
        print(fin8)

        # am I stupid? yeah probably

    if len(a_list) > 10:
        new_list = filter(lambda e: e % 2 == 0, a_list)
        # makes a new list with the existing numbers in a_list
        # only even ones added with lambda
        print (sum(list(new_list)))

function_examiner([f, g, h], [1,3,5,7,9], [min, sum, max])

"""

def function_examiner(functions, numbers, summarizers):

    # looping over functions
    for i in range(len(functions)):
        func = functions[i]
        
        # map i-th function
        func_mapped = list(map(func, numbers))

        # empty list for results
        temp = []

        # needs to repeat in function and summarizer
        for j in range(len(summarizers)):

            # list of the summarizers
            summ = summarizers[j]

            # print(reduce(summ, func_mapped), end = " ")
            temp.append(reduce(summ, func_mapped))
        print(temp)


function_examiner([f,g,h], range(100), [min,max])


# 0e) Use the filter function and function_examiner to print the sum
#   of your function on all of the even numbers up to 100.
# In other words, use filter and range to compute

print("*** 0e below ***")

def is_even(x):
    if (x % 2 == 0):
        return True
    else:
        return False

function_examiner([f,g,h], list(filter(is_even, range(100))), [min, max])
            

# function_examiner([f, g, h], [0, 2, 4, 6, 8, 10, 12, 14, 16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,96,98,100],[sum])
