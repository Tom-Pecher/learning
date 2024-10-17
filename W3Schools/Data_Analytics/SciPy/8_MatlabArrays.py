
# PYTHON: W3Schools - SciPy Tutorial
# Section 8: Matlab Arrays

from scipy import io
import numpy as np

# BASICS
    # We can save an array in a matlab file like so:
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9,])
io.savemat('Python/W3Schools/SciPy_Tutorial/example_files/arr.mat', {"vec": arr})

    # And load it as follows:
mydata = io.loadmat('Python/W3Schools/SciPy_Tutorial/example_files/arr.mat')
print("1.", mydata)

    # To load just the contained array, we must call the vec attribute:
print("2.", mydata['vec'])

    # However on its own, this increases the dimension, so to prevent this we must set squeeze_me to True:
mydata = io.loadmat('Python/W3Schools/SciPy_Tutorial/example_files/arr.mat', squeeze_me=True)
print("3.", mydata['vec']) 
