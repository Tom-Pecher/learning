
# PYTHON: W3Schools - SciPy Tutorial
# Section 10: Significance Tests

import numpy as np
from scipy.stats import ttest_ind, kstest, describe, skew, kurtosis, normaltest

# BASICS
    # We can use ttest_ind() to test if two distributions are the same:
v1 = np.random.normal(size=100)
v2 = np.random.normal(size=100)
res = ttest_ind(v1, v2)
print("1.", res)

    # To obtain just the test value, we must call the pvalue attribute:
res = ttest_ind(v1, v2).pvalue
print("2.", res)

    # We can use kstest() to test if a random variable follows a distribution:
v = np.random.normal(size=100)
res = kstest(v, 'norm')
print("3.", res)


# STATISTICAL DATA
    # To obtain important distribution data such as mean, variance and skew, we can use describe():
v = np.random.normal(size=100)
res = describe(v)
print("4.", res)

    # We can also call the individual functions for each distribution property:
v = np.random.normal(size=100)
print("5.", skew(v))
print("6.", kurtosis(v))

    # We can use normaltest() to see if a random variable comes from a normal distribution:
v = np.random.normal(size=100)
print("7.", normaltest(v))
