# List Comprehension

# Create a matrix using lists.
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

# View the matrix.
print(matrix)

# View the items in column 2.

# "build a new list by running an expression on each item in a sequence,
# one at a time, from left to right." - Learning Python

# Create a variable called col2 that takes the second item from
# each row (i.e. nested list) in the list matrix
col2 = [row[1] for row in matrix]

# View the column.
print(col2)

# Grab the diag
diag = [matrix[i][i] for i in [0, 1, 2]]

# Print it
print(diag)
