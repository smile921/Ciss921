# Built-In Object Types

# Numbers

# Add two numbers togther.
x = 493

# View the object x.
print(x)

# Strings

# Create a single
warning = "There is an earthquake in the Pacific."

# View the object "warning"
print(warning)

# View the first letter of the "warning" string variable.
print(warning[0])

# View the last letter of the "warning" string variable.
print(warning[-1])

# View the number of characters in the "warning" string variable.
print(len(warning))

# Lists

# Create a list of strings.
employees = ["Jake", "Steve", "Sarah"]

# View the first element the list.
print(employees[0])

# Add two new employees to the list.
employees = employees + ["Bill", "Stan"]

# View the entire new list of employees.
print(employees)

# Dictionaries

# Create a dictionary of greetings
greetings = {
	'English': 'Hello',
	'Spanish': 'Hola'
}

# View the greetings dictionary
print(greetings)

# Tuples

# Create a toople

dates = (12, 15, 92)

# Files

# Open a new file in output mode.
f = open('data.txt')

# Close out the file connection.
f.close()

# Find Out An Object's Type

print(type(dates))
