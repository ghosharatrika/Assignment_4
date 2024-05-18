"""
     This code generates a sample from the target distribution using markov chain 
     monte carlo method by using a gaussian as a proposal function. It then plots
     density histogram of the samples and compares with the original target PDF. 
     Also, it also plots the markov chains
"""

import numpy as np
import matplotlib.pyplot as plt


# Defining the target PDF
def target_PDF(x):
    if 3 < x < 7:
        return 1
    else:
        return 0


N = 50000  # Sample size 
sigma = 1.0  # Variance of the proposal PDF
theta = 5.0  # Starting value of the markov chain


# Defining the Metropolis algorithm
def metropolis_sampling(target_PDF, num, initial_theta, sigma):
    theta = [initial_theta]

    for _ in range(1, num):
        theta_prime = np.random.normal(theta[-1], sigma)
        r = np.random.rand()

        if target_PDF(theta_prime) / target_PDF(theta[-1]) > r:
            theta.append(theta_prime)
        else:
            theta.append(theta[-1])
    return theta


# Generating the samples using metropolis algorithm
samples = metropolis_sampling(target_PDF, N, theta, sigma)

# Plotting the markov chains
plt.plot(samples, lw=0.3)
plt.title('Markov Chain')
plt.xlabel('Iteration')
plt.ylabel('Sample value')
plt.show()
# Plotting the density histogram
plt.hist(samples, bins=50, density=True, color="blue", edgecolor='black',label='MCMC')
x = np.linspace(0, 10, 1000)
y = np.array([target_PDF(val) for val in x]) / 4.
plt.plot(x, y, color='Red', label='Target Distribution') # Plotting the target distribution
plt.title('Histogram of theta with Target Distribution')
plt.xlabel('theta')
plt.ylabel('Density')
plt.legend()
plt.show()
