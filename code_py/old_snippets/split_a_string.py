# Splitting Up A String

# Import pandas as pd.
import pandas as pd

# Create a string that contains a bunch of commas.
string_example = '0,1,1,1,1,0'

# Create a variable that is a pandas series (in R, a numeric vector) whose
# values are the numeric values split up by the string.
binary_variable = pd.Series([string_example.split(',')])

# Print the resulting numeric series
print(binary_variable)
