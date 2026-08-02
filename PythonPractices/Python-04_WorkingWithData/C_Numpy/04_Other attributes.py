# import numpy library
import numpy as np 

# Create a numpy array
a = np.array([0, 1, 2, 3, 4])
print(a)

# Get the size of numpy array
print(a.size)

# Get the number of dimensions of numpy array
print(a.ndim)

# Get the shape/size of numpy array
print(a.shape)


#---- STATISTICAL FUNCTIONS

# Create a numpy array
a = np.array([1, -1, 1, -1])
print(a)

# Get the mean of numpy array
mean = a.mean()
print(mean)

# Get the standard deviation of numpy array
standard_deviation=a.std()
print(standard_deviation)

# Create another numpy array
b = np.array([-1, 2, 3, 4, 5])
print(b)

# Get the biggest value in the numpy array
max_b = b.max()
print(max_b)

# Get the smallest value in the numpy array
min_b = b.min()
print(min_b)

