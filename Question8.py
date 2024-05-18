"""
     This code is used to calculate integral to find the volume of N-dimensional
     sphere with unit radius using Monte Carlo integration method.
"""

# Calculating the integral using Monte Carlo integration
def monte_carlo_estimate(N, D):
    count = 0
    for _ in range(N):
        points = np.random.uniform(-1, 1, D)
        if np.sum(points**2) <= 1:
            count += 1
    estimate = (count / N) * (2**D)
    return estimate


num_samples = 100000  # Sample sizes

# Calculating the area of a unit circle
dimensions = 2
circle_area = monte_carlo_estimate(num_samples, 2)
print(f"Estimated area of the unit circle: {circle_area}")

# Calculating the volume of a 10-dimensional unit sphere
dimensions = 10
sphere_volume = monte_carlo_estimate(num_samples, dimensions)
print(f"Estimated volume of the 10-dimensional unit sphere: {sphere_volume}")
