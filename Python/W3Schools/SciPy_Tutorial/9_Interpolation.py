
# PYTHON: W3Schools - SciPy Tutorial
# Section 9: Interpolation

from scipy.interpolate import interp1d, UnivariateSpline, Rbf
import numpy as np

# BASICS
    # We can use interp1d() to perform linear interpolation and then enter values into the approximation:
xs = np.arange(10)
ys = 2*xs + 1
interp_func = interp1d(xs, ys)
newarr = interp_func(np.arange(2.1, 3, 0.1))
print("1.", newarr)

    # We can use UnivariateSpline() to fit a piecewise polynomial curve to the data and then enter values into the approximation:
xs = np.arange(10)
ys = xs**2 + np.sin(xs) + 1
interp_func = UnivariateSpline(xs, ys)
newarr = interp_func(np.arange(2.1, 3, 0.1))
print("2.", newarr)

    # We can use Rbf() to fit a radial basis function to the data and then enter values into the approximation:
xs = np.arange(10)
ys = xs**2 + np.sin(xs) + 1
interp_func = Rbf(xs, ys)
newarr = interp_func(np.arange(2.1, 3, 0.1))
print("3.", newarr)
