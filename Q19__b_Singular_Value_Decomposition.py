import numpy as np
import time

# Define the matrix
A = np.array([[2, 1],
              [1, 0],
              [0, 1]])

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


'''
out put :


Matrix A:
[[2 1]
 [1 0]
 [0 1]]

Singular Value Decomposition (SVD) with rounded singular values:
U:
[[-9.12870929e-01  5.55111512e-17 -4.08248290e-01]
 [-3.65148372e-01 -4.47213595e-01  8.16496581e-01]
 [-1.82574186e-01  8.94427191e-01  4.08248290e-01]]

Singular Values (S) rounded to four decimal places:
[[2.44948974 0.        ]
 [0.         1.        ]
 [0.         0.        ]]

V^T:
[[-0.89442719 -0.4472136 ]
 [-0.4472136   0.89442719]]

Reconstructed Matrix with rounded singular values:
[[ 2.  1.]
 [ 1. -0.]
 [-0.  1.]]

Time taken for computation: 0.0023326873779296875 seconds
'''