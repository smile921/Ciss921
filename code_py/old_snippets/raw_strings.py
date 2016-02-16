# Raw Strings

# Because \n is an escape for newline, it can mess up strings and file paths.

# We can get around this by putting "r" before the string.

# Create a file object with the string have the r (for raw)
myfile = open(r'C:\new\text.dat', 'w')

# Alternative approach is double slashes
myfile = open('C:\\new\\text.dat', 'w')
