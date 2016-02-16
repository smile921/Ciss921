# Functions Basics
# Based on Byte of Python

# Create a function called printMax with the paramaters x and y.
def printMax(x, y):
    # if a is larger than b
    if x > y:
        # then print this
        print(x, 'is maximum')
    # if a is equal to b
    elif x == y:
        # print this
        print(x, 'is equal to', y)
    # otherwise
    else:
        # print this
        print(y, 'is maximum')

# Run the function with two arguments
printMax(3,4)

# Note: By default, variables created within functions are local to
# the function. But you can create a global function that IS defined outside
# the function.

# Create a variable called x
x = 50

# Create a function called func()
def func():
    # Create a global variable called x
    global x

    # Print this
    print('x is', x)
    # Set x to 2.
    x = 2
    # Print this
    print('Changed global x to', x)

# Run the func() function
func()

# Print x
print(x)

# Default Argument Values

# Create a function called say() that displays x with the default value of 1
def say(x, times = 1, times2 = 3):
    print(x * times, x * times2)

# Run the function say() with the default values
say('!')

# Run the function say() with the non-default values of 5 and 10
say('!', 5, 10)

# VarArgs Parameters (i.e. unlimited number of parameters)
# * denotes that all positonal arguments from that point to next arg are used
# ** dnotes that all keyword arguments from that point to the next arg are used

# Create a function called total() with three parameters
def total(initial=5, *numbers, **keywords):
    # Create a variable called count that takes it's value from initial
    count = initial
    # for each item in numbers
    for number in numbers:
        # add count to that number
        count += number
    # for each item in keywords
    for key in keywords:
        # add count to keyword's value
        count += keywords[key]
    # return counts
    return count

# Run total().
# 10 is for initial.
# 1,2,3 are for *numbers.
# vegetables and fruit is for **keywords.
print(total(10, 1, 2, 3, vegetables=50, fruits=100))

# DocStrings (outputs documentation about a function)

# Create a function called printMax with the paramaters x and y.
def printMax(x, y):
    # Create the docstring
    '''Prints out the maximum of two values'''
    # if a is larger than b
    if x > y:
        # then print this
        print(x, 'is maximum')
    # if a is equal to b
    elif x == y:
        # print this
        print(x, 'is equal to', y)
    # otherwise
    else:
        # print this
        print(y, 'is maximum')

# Run the function with two arguments
printMax(3,4)

# View the docstring
print(printMax.__doc__)
