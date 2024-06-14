
# PYTHON: W3Schools - SciPy Tutorial
# Section 5: Sparse Data

import numpy as np
from scipy.sparse import csr_matrix

# BASICS
    # Sparse data is a data set where most of the item values are zero.
    # There are primarily two types of sparse matrices that we use:
    #    CSC - Compressed Sparse Column: for efficient arithmetic, fast column slicing.
    #    CSR - Compressed Sparse Row: for fast row slicing, faster matrix vector products


# CSR MATRICES:
    # In a CSR matrix, each non-zero item is preceeded by its position (the 2 is in the 0th row at position 8):
arr = np.array([0, 0, 0, 0, 0, 1, 1, 0, 2])
print("1.", csr_matrix(arr))

    # We can view the data stored in the CSR matrix with the data attribute:
print("2.", csr_matrix(arr).data)

    # We can count the entries with count_nonzero():
print("3.", csr_matrix(arr).count_nonzero())

    # We may eliminate zero entries from a matrix using eliminate_zeros():
arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])
mat = csr_matrix(arr)
mat.eliminate_zeros()
print("4.", mat)

    # We may also eliminate duplicate entries from the matrix using sum_duplicates():
arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])
mat = csr_matrix(arr)
mat.sum_duplicates()
print("5.", mat)

    # Finally, we can also convert from CSR to CSC using tocsc():
arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])
newarr = csr_matrix(arr).tocsc()
print("6.", newarr)

# NOTE: sparse matrices support all of the operations that normal matrices support e.g. reshaping, summing, arithemetic, broadcasting etc.
