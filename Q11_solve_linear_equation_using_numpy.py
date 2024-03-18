import numpy as np
#first system of equation
A1 = np.array([[3, -1, 1],
              [3, 6, 2],
              [3, 3, 7]])

b1 = np.array([1, 0, 4])
#second system of equation
A2 = np.array([[10, -1, 0],
              [-1, 10, -2],
              [0, -2, 10]])


b2 = np.array([9, 7, 6])
# third system of equation
A3 = np.array([[10, 5, 0, 0],
              [5, 10, -4, 0],
              [0, -4, 8, -1],
              [0, 0, -1, 5]])

b3 = np.array([6, 25, -11, -11])
#fourth system of equation
A4 = np.array([[4, 1, 1, 0, 1],
              [-1, -3, 1, 1, 0],
              [2, 1, 5, -1, -1],
              [-1, -1, -1, 4, 0],
              [0, 2, -1, 1, 4]])

b4 = np.array([6, 6, 6, 6, 6])

solution1= np.linalg.solve(A1, b1)
solution2= np.linalg.solve(A2, b2)
solution3= np.linalg.solve(A3, b3)
solution4= np.linalg.solve(A4, b4)
print(" Print the  first system of equation solution")
("Solution1:")
print("x1 =", solution1[0])
print("x2 =", solution1[1])
print("x3 =", solution1[2])

print ("the second system of equation solution") 
("Solution2:")
print("x1 =", solution2[0])
print("x2 =", solution2[1])
print("x3 =", solution2[2])

print ("the third system of equation solution ")
("Solution3:")
print("x1 =", solution3[0])
print("x2 =", solution3[1])
print("x3 =", solution3[2])
print("x4 =", solution3[3])

print ("the fourth system of equation solution ")
("Solution4:")
print("x1 =", solution4[0])
print("x2 =", solution4[1])
print("x3 =", solution4[2])
print("x4 =", solution4[3])
print("x5 =", solution4[4])