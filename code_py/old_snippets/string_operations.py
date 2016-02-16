# String Operations

# Python 3 has three string types
# str() is for unicode
# bytes() is for binary data
# bytesarray() mutable variable of bytes

# Create some simulated text.
string = 'The quick brown fox jumped over the lazy brown bear.'

# Capitalize the first letter.
string_capitalized = string.capitalize()
print(string_capitalized)

# Center the string with periods on either side, for a total of 79 characters
string_centered = string.center(79, '.')
print(string_centered)

# Count the number of e's between the fifth and last character
string_counted = string.count('e', 4, len(string))
print(string_counted)

# Locate any e's between the fifth and last character
string_find = string.find('e', 4, len(string))
print(string_find)

# Are all characters are alphabet?
string_isalpha = string.isalpha()
print(string_isalpha)

# Are all characters digits?
string_isdigit = string.isdigit()
print(string_isdigit)

# Are all characters lower case?
string_islower = string.islower()
print(string_islower)

# Are all characters numeric?
string_isnumeric = string.isnumeric()
print(string_isnumeric)

# Are all characters decimal?
string_isdecimal = string.isdecimal()
print(string_isdecimal)

# Are all chracters alphanumeric?
string_isalnum = string.isalnum()
print(string_isalnum)

# Are all characters whitespaces?
string_isalnum = string.isspace()
print(string_isalnum)

# Is the string properly titlespaced?
string_istitle = string.istitle()
print(string_istitle)

# Are all the characters uppercase?
string_isupper = string.isupper()
print(string_isupper)

# Return the lengths of string
print(len(string))

# Convert string to lower case
string_lower = string.lower()
print(string_lower)

# Convert string to lower case
string_upper = string.upper()
print(string_upper)

# Convert string to title case
string_title = string.title()
print(string_title)

# Convert string the inverted case
string_swapcase = string.swapcase()
print(string_swapcase)

# Remove all leading whitespaces (i.e. to the left)
string_lstrip = string.lstrip()
print(string_lstrip)

# Remove all leading and trailing whitespaces (i.e. to the left and right)
string_strip = string.strip()
print(string_strip)

# Remove all trailing whitespaces (i.e. to the right)
string_rstrip = string.rstrip()
print(string_rstrip)

# Replace lower case e's with upper case E's, to a maximum of 4
string_replace = string.replace('e', 'E', 4)
print(string_replace)
