import numpy as np
import time

# Define the matrix
A = np.array([[0,1,1],
              [0,1,0],
              [1,1,0],
              [0,1,0],
              [1,0,1]])

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
[[0 1 1]
 [0 1 0]
 [1 1 0]
 [0 1 0]
 [1 0 1]]

Singular Value Decomposition (SVD) with rounded singular values:
U:
[[-5.47722558e-01 -1.11022302e-16  7.07106781e-01 -1.32058463e-01
  -4.27271064e-01]
 [-3.65148372e-01  4.08248290e-01  1.38777878e-16 -5.43516408e-01
   6.36073827e-01]
 [-5.47722558e-01  1.38777878e-16 -7.07106781e-01 -1.32058463e-01
  -4.27271064e-01]
 [-3.65148372e-01  4.08248290e-01  1.80411242e-16  8.07633333e-01
   2.18468301e-01]
 [-3.65148372e-01 -8.16496581e-01  0.00000000e+00  1.32058463e-01
   4.27271064e-01]]

Singular Values (S) rounded to four decimal places:
[[2.23606798 0.         0.        ]
 [0.         1.41421356 0.        ]
 [0.         0.         1.        ]
 [0.         0.         0.        ]
 [0.         0.         0.        ]]

V^T:
[[-4.08248290e-01 -8.16496581e-01 -4.08248290e-01]
 [-5.77350269e-01  5.77350269e-01 -5.77350269e-01]
 [-7.07106781e-01  2.22044605e-16  7.07106781e-01]]

Reconstructed Matrix with rounded singular values:
[[-0.  1.  1.]
 [-0.  1. -0.]
 [ 1.  1. -0.]
 [-0.  1. -0.]
 [ 1. -0.  1.]]

Time taken for computation: 0.0028400421142578125 seconds

'''