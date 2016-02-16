# Save A Matplotlib Plot As A Vector

# Import Numpy and matplotlib.pyplot
import numpy as np
import matplotlib.pyplot as plt

# Create two new variables for mu and sigma
mu, sigma = 100, 15

# Create some simulated data of 10000 values
x = mu + sigma * np.random.randn(10000)

# Create a histogram of the simulated data.
n, bins, patches = plt.hist(x, 50, normed=1, facecolor='g', alpha=0.75)

# Set the x axis label.
plt.xlabel('Smarts')

# Set the y axis label.
plt.ylabel('Probability')

# Set the plot title.
plt.title('Histogram of IQ')

# Add some text in the corner.
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')

# Set the axes
plt.axis([40, 160, 0, 0.03])

# Display the grid.
plt.show()

# Save the plot as an EPS vector file.
plt.savefig("example_plot.eps", format="eps")