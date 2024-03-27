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
print(reconstructed_A)
print("\nTime taken for computation: {} seconds".format(end_time - start_time))



'''
Matrix A:
[[2 1]
 [1 0]]

Singular Value Decomposition (SVD):
U:
[[-0.92387953 -0.38268343]
 [-0.38268343  0.92387953]]

Singular Values (S):
[[2.41421356 0.        ]
 [0.         0.41421356]]

V^T:
[[-0.92387953 -0.38268343]
 [ 0.38268343 -0.92387953]]

Reconstructed Matrix:
[[ 2.00000000e+00  1.00000000e+00]
 [ 1.00000000e+00 -5.55111512e-17]]

Time taken for computation: 0.0010044574737548828 seconds
'''