"""
    This code generates the random numbers which are uniformly distributed in the
    range [0,1] using linear congruential generator method. Then it plots the 
    histogram of the sample and compares with the PDF of the uniform distribution.
"""

import numpy as np
import matplotlib.pyplot as plt
import time

m = 50000
a = 1241
c = 502
seed = 2500

N = 10000
# Initialize the random number list with the seed
random_numbers = []
x = seed

# Measure the time taken to generate random numbers using LCG
start_time = time.time()

# Calculating Random numbers using Linear Congruential Generator
for i in range(N):
    x = (a * x + c) % m
    random_numbers.append(x / m)

end_time = time.time()
lcg_time = end_time - start_time
print(f"Time taken by LCG to generate {N} random numbers: {lcg_time} seconds")

# Defining the Uniform PDF
x = np.linspace(0, 1, 100)
uniform_pdf = np.ones_like(x)

# Plotting the result
plt.plot(x, uniform_pdf, color='red', lw=2, label='Uniform PDF')
plt.hist(np.array(random_numbers), bins=50, density=True, color='skyblue', edgecolor='black', label='Random no generated using LCG')
plt.title('Density Histogram of LCG Random Numbers')
plt.xlabel('Value')
plt.ylabel('Density')
plt.legend()
plt.show()
