# Set The Color Of A Matplotlib

# Import numpy and matplotlib.pyplot.
import numpy as np
import matplotlib.pyplot as plt

# Create some simulated data.
n = 100
r = 2 * np.random.rand(n)
theta = 2 * np.pi * np.random.rand(n)
area = 200 * r**2 * np.random.rand(n)
colors = theta

# Create a scatterplot using the RdYlGn colormap.
# Full list of colormaps: http://wiki.scipy.org/Cookbook/Matplotlib/Show_colormaps
c = plt.scatter(theta, r, c=colors, s=area, cmap=plt.cm.RdYlGn)

# View the plot.
plt.show()