"""
    This code generates a sample of random numbers distributed as gaussian 
    with mean = 0 and variance = 1 using Box Muller method. Then it plots
    the histogram of the sample and compares it with the gaussian PDF.
"""

import numpy as np
import matplotlib.pyplot as plt

mean = 0
variance = 1

N = 10000  # Sample size

# Generating Gaussian random no. using Box Muller Method

# Generating two uniformly distributed random no.
x1 = np.random.rand(N)
x2 = np.random.rand(N)
# Transforming the uniform random nos. to random no. distributed as gaussian distribution
y = mean + np.sqrt(variance) * np.sqrt(-2 * np.log(x1)) * np.cos(2 * np.pi * x2)

# Calculating the Gaussian PDF
x = np.linspace(-5, 5, 1000)
gaussian_pdf = 1 / np.sqrt(2 * np.pi * variance) * np.exp(- (x - mean) ** 2 / (2 * variance))

# Plotting the result
plt.plot(x, gaussian_pdf, color='blue', lw=2, label='Gaussian PDF')
plt.hist(y, bins=50, density=True, color='orange', edgecolor='black', label='Gaussian Random no.')
plt.title('Density Histogram of Gaussian Random Numbers')
plt.xlabel('Value')
plt.ylabel('PDF')
plt.legend()
plt.show()
