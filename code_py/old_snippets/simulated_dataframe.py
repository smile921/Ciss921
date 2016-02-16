# Create a simple dataframe with simulated values

# Import pandas and numpy.
import pandas as pd
import numpy as np

# Create a dataframe of 3 columns of 8 random values. 
# The dataframe has row index (i.e. row names) of dates and the columns A, B, C
df = pd.DataFrame(np.random.randn(100, 3), index=pd.date_range('1/1/2000', 
                  periods=100), columns=['A', 'B', 'C'])

# View the first four lines of the dataframe.
print(df[0:4])

# View the value in the 1st row and the "A" column.
print(df['A'][0])