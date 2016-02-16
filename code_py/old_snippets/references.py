# A Note About References

# Create a variable of countries
countries = ['USA', 'UK', 'France', 'Kenya']

# Create a variable that references countries
nation_states = countries

# Create a variables that copies all the items inside countries via slicing
un_members = countries[:]

# Print all three variables
print(nation_states)
print(countries)
print(un_members)

# Print the first item in counties
del countries[0]

# Print the first item in counties
del nation_states[-1]

# Print all three variables
print(nation_states)
print(countries)
print(un_members)

# Notice that both countries and nation_states have had their first and last
# items removed, because they both reference the same items in memory. However,
# un_members still contains all the countries because it copied all items.

