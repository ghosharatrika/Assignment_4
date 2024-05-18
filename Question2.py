"""
    This code generates the random numbers which are uniformly distributed in the
    range [0,1] using numpy.random.rand(). Then it plots the histogram of the sample 
    and compares with the PDF of the uniform distribution.

    Additionally it also calculates the time to generate the uniformly distributed sample.
"""

import numpy as np
import matplotlib.pyplot as plt
import time

N = 10000  # Sample size
random_number = np.zeros(N)

# Measuring the time taken to generate random numbers using numpy function
start_time = time.time()

for i in range(N):
    random_number[i] = np.random.rand()  # Generating uniformly distributed random numbers

end_time = time.time()
numpy_time = end_time - start_time
print(f"Time taken by numpy.random.rand to generate {N} random numbers: {numpy_time} seconds")

# Defining the Uniform PDF
x = np.linspace(0, 1, 100)
uniform_pdf = np.ones_like(x)

# Plotting the result
plt.plot(x, uniform_pdf, color='blue', lw=2, label='Uniform PDF')
plt.hist(random_number, bins=50, density=True, color='pink', edgecolor='black', label='Random no generated using numpy')
plt.title('Density Histogram of np.random.rand() Random Numbers')
plt.xlabel('Value')
plt.ylabel('Density')
plt.legend()
plt.show()
