"""
    This code checks for the randomness of the random variable by employing
    the chi-squared test and also labels the random as "not sufficiently random",
    "suspect","almost suspect", and "sufficiently random" using the p value.
"""

import numpy as np
from scipy.stats import chi2

# Using p value to determine whether the random variable is sufficiently random or not
def determine_label(p_value):
    if p_value < 0.01:
        return "not sufficiently random"
    elif p_value < 0.05:
        return "suspect"
    elif p_value < 0.10:
        return "almost suspect"
    else:
        return "sufficiently random"


# Observed counts for two runs
observed_counts1 = np.array([4, 10, 10, 13, 20, 18, 18, 11, 13, 14, 13])
observed_counts2 = np.array([3, 7, 11, 15, 19, 24, 21, 17, 13, 9, 5])

total_observations = np.sum(observed_counts1)
expected_probabilities = np.array([1/36, 2/36, 3/36, 4/36, 5/36, 6/36, 5/36, 4/36, 3/36, 2/36, 1/36])
expected_counts = expected_probabilities * total_observations

# Chi-square statistic calculation
chi2_statistic1 = np.sum((observed_counts1 - expected_counts) ** 2 / expected_counts)
chi2_statistic2 = np.sum((observed_counts2 - expected_counts) ** 2 / expected_counts)

print("Chi square statistic for run 1: ", chi2_statistic1)
print("Chi square statistic for run 2: ", chi2_statistic2)

df = 10
# Calculating p value for the runs
p_value1 = 1 - chi2.cdf(chi2_statistic1, df)
p_value2 = 1 - chi2.cdf(chi2_statistic2, df)

label1 = determine_label(p_value1)
label2 = determine_label(p_value2)

print("The random variable for run 1:", label1)
print("The random variable for run 2:", label2)
