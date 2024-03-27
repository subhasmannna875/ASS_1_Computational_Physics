import numpy as np
import time

# Define the matrix
A = np.array([[2, 1],
              [-1,1],
              [1,1],
              [2,-1]])

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

out put:


Matrix A:
[[ 2  1]
 [-1  1]
 [ 1  1]
 [ 2 -1]]

Singular Value Decomposition (SVD) with rounded singular values:
U:
[[-0.63245553 -0.5        -0.52229321 -0.27786652]
 [ 0.31622777 -0.5        -0.30196857  0.74753928]
 [-0.31622777 -0.5         0.79704714  0.12130893]
 [-0.63245553  0.5        -0.02721464  0.59098169]]

Singular Values (S) rounded to four decimal places:
[[3.16227766 0.        ]
 [0.         2.        ]
 [0.         0.        ]
 [0.         0.        ]]

V^T:
[[-1. -0.]
 [-0. -1.]]

Reconstructed Matrix with rounded singular values:
[[ 2.  1.]
 [-1.  1.]
 [ 1.  1.]
 [ 2. -1.]]

Time taken for computation: 0.0029964447021484375 seconds
'''