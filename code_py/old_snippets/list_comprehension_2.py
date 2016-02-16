# List Comprehension 2
# Based on http://datasciencelab.wordpress.com/2014/01/08/list-comprehension-in-python/

# First Letter Of Every Word

# Import the string module
import string

# Create a variable that includes all punctuation and adds a blank space
# string.punctuation is: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
punct = string.punctuation + ' '

# Create a string for all vowels
vowels = 'aeiou'

# Create some text
phrase = 'Strictly speaking Python strings are categorized as immutable sequences'

# Create a variable for the first letter in every word of phase, after split up
first_letter = [w[0] for w in phrase.split()]

# Print it out
print(first_letter)

# In the above example here is the breakdown of the list Comprehension

# [w[0]             is the output. That is, what we want done.
# for w in          is the iterator identifier
# phrase.split()]   is the input

# You can also add a conditional statement

# Create some simulated numbers
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Create a variable called output that squared every element in numbers variable
# if it is divisible by 2
output = [x**2 for x in numbers if x%2 == 0]

# View the output
print(output)
