# List Operations

# Create a list of simulated data.
countries = ["Spain", "Japan", "Kenya", "Tanzania", "Ghana"]

# Add an item to the end of the list.
# Note: If the appending item contains multiple items, it is nested.
countries.append("Nigeria"); print(countries)

# Add all items of a list to a list
countries.extend(["France", "Switzerland", "China"]); print(countries)

# Insert Italy into the second position of the list countries
countries.insert(1, "Italy"); print(countries)

# Remove Spain from the list countries
countries.remove("Spain"); print(countries)

# Delete the second item from the list countries
del countries[1]; print(countries)

# Remove the third item from the list, and returns it (i.e. "pops it out")
print(countries)
print(countries.pop(3))
print(countries)

# Return the index of the first item that matches "Kenya"
kenya = countries.index("Kenya"); print(kenya)

# Count all number of times "Kenya" appears in the list countries
kenya_count = countries.count("Kenya"); print(kenya_count)

# Sort the list in alphabetical order
countries.sort(); print(countries)

# Reverse the elements of the list
countries.reverse(); print(countries)

# Copy the list, same as countries[:]
countries_copy = countries.copy(); print(countries_copy)

# Remove all the items from the list countries
countries.clear(); print(countries)
