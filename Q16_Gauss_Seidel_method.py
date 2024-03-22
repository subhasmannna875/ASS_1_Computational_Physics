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

# Initial guess
x = np.zeros_like(b, dtype=float)


#  initial guess of Number of iterations
num_iterations =1000 

# Perform iterations
for k in range(num_iterations):
    x_new=np.zeros_like(b, dtype=float)
    for i in range(len(x)):
        sum1 = np.dot(A[i, :i], x_new[:i])
        sum2 = np.dot(A[i, i+1:], x[i+1:])
        x_new[i] =  (1 / A[i, i]) * (b[i] - sum1 - sum2)
    x = np.copy(x_new)
    #break the loop when we reached solution  bellow tollerence   // using relative infinity norm error 
    if np.max(np.abs(x_new - x_act)) / np.max(np.abs(x_act)) < 0.01:
        break
print("solution:",x)
print("number of iteration:",k+1)


'''

OUT PUT 

solution: [ 7.79173672  0.42195986 -0.07247764 -0.53199167  0.01057853]
number of iteration: 12
'''