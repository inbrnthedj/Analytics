# import numpy library
import numpy as np 

# ---- OPERATIONS

# declare arrays
u = np.array([1, 0])
v = np.array([0, 1])
print(u)
print(v)

# Numpy Array Addition
z = np.add(u, v)
print(z)


# ADDITION
arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])

arr3 = np.add(arr1,arr3)
print(arr3)


# SUBTRACTION
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([20, 21, 22, 23, 24, 25])

arr3 = np.subtract(arr1,arr2)
print(arr3)

# MULTIPLICATION
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([2, 1, 2, 3, 4, 5])

arr3 = np.multiply(arr1,arr2)
print(arr3)


# DIVISION
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 5, 10, 8, 2, 33])

arr3 = np.divide(arr1,arr2)
print(arr3)

# DOT PRODUCT
arr1 = np.array([3, 5])
arr2 = np.array([2, 4])

arr3 = np.dot(arr1,arr2)
print(arr3)


# ADDING CONSTANT

# Create a constant to numpy array
u = np.array([1, 2, 3, -1]) 
print(u)

# Add the constant to array
print(u + 1)

