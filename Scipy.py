from scipy import linalg
import numpy as np

#Declaring the numpy arrays
a = np.array([[-1,2], [3,4]])
b = np.array([3,11])
#Passing the values to the solve function
x = linalg.solve(a, b)
#printing the result array
print(x)
#Finding Determinant
#Declaring the numpy array
A = np.array([[1,2],[3,4]])
#Passing the values to the det function
x = linalg.det(A)
#printing the result
print(x)

