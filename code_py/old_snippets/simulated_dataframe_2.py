# Create a dataframe of simulated data

# Import numpy and pandas.
import numpy as np
import pandas as pd

# Create a set of variables as numpy arrays.
first_name = pd.Series(['Steve', 'Jason', 'Jake', 'Andy', 'Bill', 'Sarah',
						'Mindy', 'Jennifer', 'Lacy', 'Joan'])
last_name = pd.Series(['Anderson', 'Smith', 'Miller', 'Baker', 'Alyona',
					   'Black', 'Jacobson', 'Drinkerson', 'Rurrey',
					   'Morehouse'])
scores_pre = pd.Series([235.34, 928.23, 94.29, 943, 304, 405.45, 932.94,
						823.45, 473.68, 382.48])
scores_post = pd.Series([523.34, 523.23, 732.29, 523, 63, 23.45, 634.94,
						345.45, 654.68, 123.48])
treatment_group = pd.Series([0, 0, 0, 1, 1, 0, 1, 1, 0, 1])
gender = pd.Series(['M', 'M', 'M', 'M', 'M', 'F', 'F', 'F', 'F', 'F'])

# Create a dictionary variable that assigns variable names.
variable_names = dict(first_name = first_name, last_name = last_name,
					  scores_pre = scores_pre, scores_post = scores_post,
					  treatment_group = treatment_group, gender = gender)

# Create a dataframe.
experiment_data = pd.DataFrame(variable_names)

# Reorder the order of the dataframe columns
# (if we don't they are displayed in alphabetical order)
experiment_data = experiment_data[['first_name', 'last_name', 'scores_pre',
								   'scores_post', 'treatment_group', 'gender']]

# View the dataframe.
print(experiment_data)

# A shorter way to create the same dataframe.

# Create a dataset of simulated data.
ex_data = pd.DataFrame({'first_name':['Steve', 'Jason', 'Jake', 'Andy', 'Bill',
					    			  'Sarah', 'Mindy', 'Jennifer', 'Lacy',
					    			  'Joan'],
                     'last_name':['Anderson', 'Smith', 'Miller', 'Baker',
                     			  'Alyona', 'Black', 'Jacobson', 'Drinkerson',
                     			  'Rurrey', 'Morehouse'],
                     'scores_pre':[235.34, 928.23, 94.29, 943, 304, 405.45,
                     			   932.94, 823.45, 473.68, 382.48],
                     'scores_post':[523.34, 523.23, 732.29, 523, 63, 23.45,
                     				634.94, 345.45, 654.68, 123.48],
                     'treatment_group':[0, 0, 0, 1, 1, 0, 1, 1, 0, 1],
                     'gender':['M', 'M', 'M', 'M', 'M', 'F', 'F', 'F', 'F', 'F']
                       }
                      )

# Reorder the order of the dataframe columns
# (if we don't they are displayed in alphabetical order).
ex_data = ex_data[['first_name', 'last_name', 'scores_pre', 'scores_post',
				   'treatment_group', 'gender']]

# View the dataframe.
print(ex_data)
