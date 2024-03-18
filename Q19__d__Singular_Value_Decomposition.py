import numpy as np
import time

# Define the matrix
A = np.array([[1,1,0],
              [-1,0,1],
              [0,1,-1],
              [1,1,-1]])

# Time the computation of SVD
start_time = time.time()
U, S, VT = np.linalg.svd(A)
end_time = time.time()

# Determine the number of singular values
num_singular_values = min(A.shape)# minimum value of 'm'  or 'n'


# Construct the diagonal matrix from  singular values
Sigma = np.zeros_like(A, dtype=float)
Sigma[:num_singular_values, :num_singular_values] = np.diag(S)

# Compute the reconstructed matrix using rounded singular values
reconstructed_A = U @ Sigma @ VT
reconstructed_A=np.round(reconstructed_A,decimals=8)
# Print the results
print("Matrix A:")
print(A)
print("\nSingular Value Decomposition (SVD) with rounded singular values:")
print("U:")
print(U)
print("\nSingular Values (S) rounded to four decimal places:")
print(Sigma)
print("\nV^T:")
print(VT)
print("\nReconstructed Matrix with rounded singular values:")
print(reconstructed_A)
print("\nTime taken for computation: {} seconds".format(end_time - start_time))
