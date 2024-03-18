import numpy as np 
  
A = np.array([[2,-1,0], [-1,2,-1],[0,-1,2]]) 
x = np.array([[1,1,1]]).T #initial guess of eigen vector
y=np.array([2,3,4])  #any arbitary vector 
max_iter = 100
  
# Define the variable lam_prev to store the 
# previous approximation for the largest eigenvalue 
lam_prev = 0
  
for i in range(max_iter): 
    
    x = A @ x / np.linalg.norm(A @ x) #updating eigen vector after each iteration
  
    lam = (( A @ x).T)@y/ (x.T @ y)  # updating largest eigen value after each iteration
  
     
    if np.abs(lam - lam_prev)/np.abs(lam_prev) < 0.01: #  eigen value acurate wuthin 1%
        break
  
    # Store the current approximation for the largest eigenvalue 
    lam_prev = lam 
  
# Print the approximations for the 
# largest eigenvalue and eigenvector 
print("maximum eigen value:",float(lam)) 
print("eigen vector corespond to maximum eigen value:",x) 
print("number of iteration:",i+1)