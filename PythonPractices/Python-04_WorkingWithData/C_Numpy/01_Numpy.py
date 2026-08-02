# import numpy library
import numpy as np 

# Create a numpy array: calls the array() function of numpy library and pass a list as an argument
a = np.array([0, 1, 2, 3, 4])

# print array
print(a)

# Print each element
print("a[0]:", a[0])
print("a[1]:", a[1])
print("a[2]:", a[2])
print("a[3]:", a[3])
print("a[4]:", a[4])

# Print each element array - for loop
for i in range(len(a)):
    print("a[", i, "] = ", a[i])

# Check the type of the array
type(a)

# Check the type of the values stored in numpy array
a.dtype

