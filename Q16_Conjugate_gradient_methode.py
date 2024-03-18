import numpy as np
x_act=np.array([7.859713071,0.422926408,-0.073592239,-0.540643016,0.010626163])
infinity_norm=np.max(np.abs(x_act))
def conjugate_gradient(A, b, x0, max_iter=1000):
    n = len(b)
    x = x0.copy()
    r = b - np.dot(A, x)
    p = r.copy()
    rsold = np.dot(r, r)

    for i in range(max_iter):
        Ap = np.dot(A, p)
        alpha = rsold / np.dot(p, Ap)
        x = x + alpha * p
        r = r - alpha * Ap
        rsnew = np.dot(r, r)
        if np.max(np.abs(x - x_act)) / np.max(np.abs(x_act)) < 0.01:
            break
        p = r + (rsnew / rsold) * p
        rsold = rsnew

    return x,i+1

# given matrix
A = np.array([[0.2,0.1,1,1,0],
              [0.1,4,-1,1,-1],
              [1,-1,60,0,-2],
              [1,1,0,8,4],
              [0,-1,-2,4,700]])
b = np.array([1,2,3,4,5])
x0=np.zeros_like(b)

# Solve the system using Conjugate Gradient method
solution = conjugate_gradient(A, b, x0)

print("Solution:", solution[0])
print("number of iteration:",solution[1])
