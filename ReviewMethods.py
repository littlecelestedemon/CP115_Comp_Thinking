#practice defining a method
#method definitions start with def
#   then the name of the method,
#   then the arguments that the method accepts
#   then a colon
#methods also generally have a return statement,
#   which feeds data into another
#   part of the program
#   tabbed over code to be in the function
#To actually run any of the code in a method, we have to call the method

#To get data out of a method, need to return data out of the "sandbox"
#EX

def three_mult (a, b ,c):
    result = a * b * c
    return result

print(three_mult (4, 19, 3))

#above is the correct way to call the method

# print(three_mult) is incorrect because it isn't calling the method
# print(result) is incorrect because result doesn't exist outside three_mult
# above gives result like <function three_mult at greui3284uiuhrg>
