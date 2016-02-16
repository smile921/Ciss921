# Sets
# Based on: Learning Python

# Create two sets.
x = set('abcde')
y = set('bdxyz')

# View the set x.
print(x)

# Difference. That is, all items not common between x and y.
print(x - y)

# Union. That is, all items in x and and all items in y, whether they are common or not.
print(x | y)

# Intersection. That is, all common items between x and y.
print(x & y)

# Membership. That is, is "e" a member of x?
print('e' in x)

# Create z, the intersection of x and y.
z = x & y

# View z.
print(z)

# Add "c" into the set z.
z.add('c')

# Remove "c" from the set z.
z.remove('c')

