"""
     This code performs Bayesian probabilistic inference using MCMC. The given data is fitted
     to a quadratic equation with the best-fit values for the parameters a, b, and c, where 
     “best-fit” is defined as the median of the posterior PDF. It also prints the one-sigma 
     uncertainties on these value. 
     A Gaussian likelihood and uniform priors is used for the 
     analysis. 
     It plots all the chains and uses the corner library to make a plot showing 
     the joint and marginalised posterior PDFs for the three model parameters. It also makes 
     a plot showing the data with the best-fit model and 200 models randomly chosen from the 
     posterior. 
"""

import numpy as np
import emcee
import corner
import matplotlib.pyplot as plt

# Reading data from data.txt
data = np.loadtxt('data.txt')
x = data[:, 1]
y = data[:, 2]
sigma = data[:, 3]


# Defining the polynomial model
def model(theta, x):
    a, b, c = theta
    return a * x**2 + b * x + c


# Defining the log likelihood function
def log_likelihood(theta, x, y, sigma):
    model_y = model(theta, x)
    return -0.5 * np.sum((y - model_y) ** 2 / sigma ** 2 + np.log(sigma ** 2))


# Defining the log prior function
def log_prior(theta):
    a, b, c = theta
    if -10 < a < 10 and -10 < b < 10 and -10 < c < 10:
        return 0.0
    return -np.inf


# Defining the log probability function
def log_probability(theta, x, y, sigma):
    lp = log_prior(theta)
    if not np.isfinite(lp):
        return -np.inf
    return lp + log_likelihood(theta, x, y, sigma)


nwalkers = 50  # Number of Markov chains
ndim = 3       # Number of parameters (a, b, c)
nsteps = 4000  # Number of steps per chain

# Initial positions of the walkers
initial = 1e-4 * np.random.randn(nwalkers, ndim)

# Setting up the sampler
sampler = emcee.EnsembleSampler(nwalkers, ndim, log_probability, args=(x, y, sigma))

sampler.run_mcmc(initial, nsteps, progress=True)
samples = sampler.get_chain()

# Flattening the chain and discarding the burn-in
flat_samples = sampler.get_chain(discard=100, thin=15, flat=True)

# Computing the best fit corresponding to median value
best_fit = np.median(flat_samples, axis=0)

# Printing the best-fit parameters and their uncertainties upto 1 sigma
print("Best-fit parameters:")
print(f"a = {best_fit[0]:.3f} ± {np.std(flat_samples[:, 0]):.3f}")
print(f"b = {best_fit[1]:.3f} ± {np.std(flat_samples[:, 1]):.3f}")
print(f"c = {best_fit[2]:.3f} ± {np.std(flat_samples[:, 2]):.3f}")

# Creating subplots for the markov chains for the three parameters
fig, axes = plt.subplots(3, sharex=True)
labels = ["a", "b", "c"]
colors = ["r", "g", "b"]  # Red for a, Green for b, Blue for c
for i in range(ndim):
    ax = axes[i]
    ax.plot(samples[:, :, i], color=colors[i], alpha=0.3)
    ax.set_xlim(0, nsteps)
    ax.set_ylabel(labels[i])
axes[-1].set_xlabel("Step number")
plt.show()

# plot showing the joint and marginalised posterior PDFs for the three model parameters
fig = corner.corner(flat_samples, labels=labels, truths=[best_fit[0], best_fit[1], best_fit[2]],
                    scatter_kwargs={"alpha": 0.5, "marker": "o"},
                    hist_kwargs={"linewidth": 1, "edgecolor": "black"},
                    label_kwargs={"fontsize": 12})
plt.show()

x_fit = np.linspace(min(x), max(x), 1000)
plt.errorbar(x, y, yerr=sigma, fmt=".k", capsize=0)

# Plotting 200 samples from the posterior
for theta in flat_samples[np.random.randint(len(flat_samples), size=200)]:
    plt.plot(x_fit, model(theta, x_fit), color="gray", alpha=0.1)

plt.plot(x_fit, model(best_fit, x_fit), label="Best fit", color='red')
plt.legend()
plt.show()
