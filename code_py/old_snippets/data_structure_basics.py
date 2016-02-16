# Data Structure Basics
# There are four: lists, truples, dictionaries, and sets

# Lists
# "A list is a data structure that holds an ordered collection of items
# i.e. you can store a sequence of items in a list." - A Byte Of Python

# Lists are mutable.

# Create a list of countries, then print the results
allies = ['USA','UK','France','New Zealand',
          'Australia','Canada','Poland']; print(allies)

# Print the length of the list
print(len(allies))

# Add an item to the list, then print the results
allies.append('China'); print(allies)

# Sort list, then print the results
allies.sort(); print(allies)

# Reverse sort list, then print the results
allies.sort(); print(allies)

# View the first item of the list
print(allies[0])

# View the last item of the list
print(allies[-1])

# Delete the item in the list
del allies[0]; print(allies)

# Add a numeric value to a list of strings
allies.append(3442); print(allies)

# Truples

# "Though tuples may seem similar to lists, they are often used in different
# situations and for different purposes. Tuples are immutable, and usually
# contain an heterogeneous sequence of elements that are accessed via unpacking
# (or indexing (or even by attribute in the case of namedtuples).
# Lists are mutable, and their elements are usually homogeneous
# and are accessed by iterating over the list." - Python Documentation

# "Tuples are heterogeneous data structures (i.e., their entries have different
# meanings), while lists are homogeneous sequences." - StackOverflow

# Parentheses are optional, but useful.

# Create a tuple of state names
usa = ('Texas', 'California', 'Maryland'); print(usa)

# Create a tuple of countries
# (notice the USA has a state names in the nested tuple)
countries = ('canada', 'mexico', usa); print(countries)

# View the third item of the top tuple
print(countries[2])

# View the third item of the third tuple
print(countries[2][2])

# Dictionaries
# "A dictionary is like an address-book where you can find the address or
# contact details of a person by knowing only his/her name i.e. we associate
# keys (name) with values (details). Note that the key must be unique just like
# you cannot find out the correct information if you have two persons with the
# exact same name." - A Byte Of Python

# Create a dictionary with key:value combos
staff = {'Chris' : 'chris@stater.org',
         'Jake' : 'jake@stater.org',
         'Ashley' : 'ashley@stater.org',
         'Shelly' : 'shelly@stater.org'
        }

# Print the value using the key
print(staff['Chris'])

# Delete a dictionary entry based on the key
del staff['Chris']; print(staff)

# Add an item to the dictionary
staff['Guido'] = 'guido@python.org'; print(staff)

# Sets
# Sets are unordered collections of simple objects.

# Create a set of BRI countries
BRI = set(['brazil', 'russia', 'india'])

# Is India in the set BRI?
'india' in BRI

# Is the US in the set BRI?
'usa' in BRI

# Create a copy of BRI called BRIC
BRIC = BRI.copy()

# Add China to BRIC
BRIC.add('china')

# Is BRIC a super-set of BRI?
BRIC.issuperset(BRI)

# Remove Russia from BRI
BRI.remove('russia')

# What items are the union of BRI and BRIC?
BRI & BRIC
