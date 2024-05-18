"""
    This code generates a sample of random variable distributed as error function
    using Rejection method. Then it plots the histogram and compares with the 
    target PDF.
"""

import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return np.sqrt(2 / np.pi) * np.exp(-x ** 2 / 2)  # Target PDF from which random no. to be sampled


N = 10000  # Sample size

# Defining exponential function to determine the acceptance area
y_uniform = np.random.rand(N)
y_exp = - 0.7 * np.log(y_uniform)
x_exp = np.random.rand(N) * 5

x_val = np.linspace(0, 5, 100)

y_good = []
x_good = []

# Filtering the random no. to select only those which are distributed as target PDF
for i in range(N):
    if y_exp[i] <= f(x_exp[i]):
        y_good.append(y_exp[i])
        x_good.append(x_exp[i])

# Plotting the accepted random no.
plt.plot(x_val, f(x_val), color='blue', label='err func')
plt.plot(x_val, np.exp(- 0.7 * x_val), color='black', label='$f(x) = e^{-0.7 * x}$')
plt.scatter(x_good, y_good, color='red', label='accepted random numbers')
plt.title("Rejection Method")
plt.xlabel('x')
plt.ylabel('PDF')
plt.legend()
plt.show()
# Plotting the histogram
plt.plot(x_val, f(x_val), label='err func')
plt.hist(x_good, bins=100, density=True, color='red', edgecolor='black', label='Random no. generated as f(x)')
plt.title("Random nos. generated as $f(x) = e^{-0.7x}$")
plt.xlabel('x')
plt.ylabel('PDF')
plt.legend()
plt.show()
