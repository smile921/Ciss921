# Assignment Operators

# Create some variables
a = 2
b = 1
c = 0
d  = 3

# Assigns values from right side to left side
c = a + b
print("c = a + b : ", c)

# adds right to the left and assigns the result to left
# c = a + c
c += a
print("c += a : ", c)

# subtracts right from the left and assigns the result to left
# c = a - c
c -= a
print("c -= a : ", c)

# multiplies right with the left and assigns the result to left
# c = a * c
c *= a
print("c *= a : ", c)
# divides left with the right and assigns the result to left
# c = c / a
c /= a
print("c /= a : ", c)

# takes modulus using two operands and assigns the result to left
# a = d % a
d %= a
print("d %= a : ", d)

# exponential (power) calculation on operators and assign value to the left
# d = d ^ a
d **= a
print("d **= a : ", d)

# floor division on operators and assigns value to the left
# d // a
# d = d // a
d //= a
print("d //= a : ", d)
