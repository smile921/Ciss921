# Test script to check the right environment is being used and one of the data science modules is installed

# Import the sys module.
import sys

# Print the path to the Python environment.
print(sys.executable)

# Run a quick test to see if numpy module is installed.
import numpy as np
arr = np.arange(100)
print(arr)

# Run a quick test to see if pandas module is installed.
import pandas as pd
df = pd.DataFrame(np.random.randn(8, 3), 
                  index=pd.date_range('1/1/2000', periods=8), 
                  columns=['A', 'B', 'C'])
print(df)

# View the first 4 rows.
print(df[0:4])