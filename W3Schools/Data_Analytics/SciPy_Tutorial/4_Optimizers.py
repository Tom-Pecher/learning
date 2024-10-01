
# PYTHON: W3Schools - SciPy Tutorial
# Section 4: Optimizers

from scipy.optimize import root, minimize
from math import cos

# FINDING ROOTS
    # To solve an equation, we can use scipy.optimize.root() and find the x attribute:
def eqn1(x):
  return x + cos(x)
myroot = root(eqn1, 0)
print("1.", myroot.x)

    # However, root() returns other information that may be useful:
print("2.", myroot)


# FINDING MINIMA:
    # To minimize a function, we can use scipy.optimize.minimize() and find the x attribute:
def eqn2(x):
  return x**2 + x + 2
mymin = minimize(eqn2, 0, method='BFGS')
print("3.", mymin.x)

    # Again, more information is provided:
print("4.", mymin)

    # We can select from a variaty of minimization algorithms (by setting method=...):
        # CG
        # BFGS
        # Newton-CG
        # L-BFGS-B
        # TNC
        # COBYLA
        # SLSQP
