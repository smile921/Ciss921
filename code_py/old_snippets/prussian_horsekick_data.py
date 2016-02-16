# Prussian Horse Kick Data

# Based on: http://www.math.uah.edu/stat/data/HorseKicks.html

# Original description: "The data above give the number of soilders in the
# Prussian cavalry killed by horse kicks, by corp membership and by year. The
# years are from 1875 to 1894, and there are 14 different cavalry corps: the
# first column corresponds to the guard corp and the other columns to corps 1
# through 11, 14, and 15. The data are from Distributome project and are derived
# from the book by Andrews and Herzberg. The original source of the data is the
# classic book by von Bortkiewicz (references are given below). The data are
# famous because they seem to fit the Poisson model reasonably well."

import pandas as pd

year = pd.Series([1875, 1876, 1877, 1878, 1879, 1880, 1881, 1882, 1883, 1884,
                  1885, 1886, 1887, 1888, 1889, 1890, 1891, 1892, 1893, 1894])
guard_corps = pd.Series([0,2,2,1,0,0,1,1,0,3,0,2,1,0,0,1,0,1,0,1])
corps_1 = pd.Series([0,0,0,2,0,3,0,2,0,0,0,1,1,1,0,2,0,3,1,0])
corps_2 = pd.Series([0,0,0,2,0,2,0,0,1,1,0,0,2,1,1,0,0,2,0,0])
corps_3 = pd.Series([0,0,0,1,1,1,2,0,2,0,0,0,1,0,1,2,1,0,0,0])
corps_4 = pd.Series([0,1,0,1,1,1,1,0,0,0,0,1,0,0,0,0,1,1,0,0])
corps_5 = pd.Series([0,0,0,0,2,1,0,0,1,0,0,1,0,1,1,1,1,1,1,0])
corps_6 = pd.Series([0,0,1,0,2,0,0,1,2,0,1,1,3,1,1,1,0,3,0,0])
corps_7 = pd.Series([1,0,1,0,0,0,1,0,1,1,0,0,2,0,0,2,1,0,2,0])
corps_8 = pd.Series([1,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,1,1,0,1])
corps_9 = pd.Series([0,0,0,0,0,2,1,1,1,0,2,1,1,0,1,2,0,1,0,0])
corps_10 = pd.Series([0,0,1,1,0,1,0,2,0,2,0,0,0,0,2,1,3,0,1,1])
corps_11 = pd.Series([0,0,0,0,2,4,0,1,3,0,1,1,1,1,2,1,3,1,3,1])
corps_14 = pd.Series([1,1,2,1,1,3,0,4,0,1,0,3,2,1,0,2,1,1,0,0])
corps_15 = pd.Series([0,1,0,0,0,0,0,1,0,1,1,0,0,0,2,2,0,0,0,0])

# Create a dictionary variable that assigns variable names.
variables = dict(year = year, guard_corps = guard_corps, corps_1 = corps_1,
                 corps_2 = corps_2, corps_3 = corps_3, corps_4 = corps_4,
                 corps_5 = corps_5, corps_6 = corps_6, corps_7 = corps_7,
                 corps_8 = corps_8, corps_9 = corps_9, corps_10 = corps_10,
                 corps_11 = corps_11 , corps_14 = corps_14,
                 corps_15 = corps_15)

# Create a dataframe, set the column order with columns=
horsekick_data = pd.DataFrame(variables, columns = ['year', 'guard_corps',
                                                    'corps_1', 'corps_2',
                                                    'corps_3', 'corps_4',
                                                    'corps_5', 'corps_6',
                                                    'corps_7', 'corps_8',
                                                    'corps_9', 'corps_10',
                                                    'corps_11', 'corps_14',
                                                    'corps_15'])

# View the dataframe.
print(horsekick_data)

