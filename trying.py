from functools import reduce

def addition(n):
    return n + n

def squared_by_2(n):
    return n * n

def sequence_examiner(the_list, num, function):
    return reduce(function, the_list)

set_list = [1,2,3,4,5]
print(list(sequence_examiner(set_list, 1, max)))
