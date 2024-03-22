import numpy as np
A = np.array([[5, -2],
              [-2, 8]])

# Perform QR decomposition
Q, R = np.linalg.qr(A)

# Calculate eigenvalues using QR decomposition
eigenvalues_qr = np.diag(R @ Q)

# Calculate eigenvalues using numpy.linalg.eigh
eigenvalues_eigh = np.linalg.eigh(A)[0]


print("Eigenvalues using QR decomposition:", eigenvalues_qr)
print("Eigenvalues using numpy.linalg.eigh:", eigenvalues_eigh)
for i in range(2):
    if eigenvalues_eigh[i]==eigenvalues_qr[i]:
        print('eigen value are equal')
    else:
        print("eigen value are different")

'''
out put 

Eigenvalues using QR decomposition: [6.79310345 6.20689655]
Eigenvalues using numpy.linalg.eigh: [4. 9.]
eigen value are different
eigen value are different

'''