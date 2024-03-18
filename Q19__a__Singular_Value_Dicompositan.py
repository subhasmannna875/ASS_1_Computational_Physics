import numpy as np
import time

# Define the matrix
A = np.array([[2, 1],
              [1, 0]])

# Time the computation of SVD
start_time = time.time()
U, S, VT = np.linalg.svd(A)
end_time = time.time()

# Compute the reconstructed matrix using SVD components
reconstructed_A = U @ np.diag(S) @ VT

# Print the results
print("Matrix A:")
print(A)
print("\nSingular Value Decomposition (SVD):")
print("U:")
print(U)
print("\nSingular Values (S):")
print(np.diag(S))
print("\nV^T:")
print(VT)
print("\nReconstructed Matrix:")
print(reconstructed_A,decimal=4)
print("\nTime taken for computation: {} seconds".format(end_time - start_time))
