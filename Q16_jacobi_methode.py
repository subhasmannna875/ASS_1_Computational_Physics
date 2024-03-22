import numpy as np
#actual_solution
x_act=np.array([7.859713071,0.422926408,-0.073592239,-0.540643016,0.010626163])
infinity_norm=np.max(np.abs(x_act))

# Define the coefficient matrix A and the constant vector b
A = np.array([[0.2,0.1,1,1,0],
              [0.1,4,-1,1,-1],
              [1,-1,60,0,-2],
              [1,1,0,8,4],
              [0,-1,-2,4,700]])
b = np.array([1,2,3,4,5])

# Decompose A into diagonal (D), lower triangular (L), and upper triangular (U) parts
D = np.diag(np.diag(A))
L = np.tril(A, k=-1)
U = np.triu(A, k=1)

# Initial guess for x
x = np.zeros_like(b)

# Jacobi iteration
max_iterations = 1000

for i in range(max_iterations):
    x_new = np.linalg.inv(D).dot(b - (L + U).dot(x))
    if np.max(np.abs(x_new - x_act)) / np.max(np.abs(x_act)) < 0.01:
        break
    x = x_new
print("Solution:", x)
print("number of iteration:",i+1)

'''
out put 

Solution: [ 7.3599123   0.40518225 -0.07236773 -0.53495951  0.01017659]
number of iteration: 19

'''
