'''
SLICING

Like lists, we can slice the numpy array. Slicing in python means taking the elements from the given index to another given index.
We pass slice like this: [start:end].The element at end index is not being included in the output.
We can select the elements from 1 to 3 and assign it to a new numpy array d as follows:

'''

# import numpy library
import numpy as np 

# Declare array
a = np.array([10, 2, 30, 40,50])
print(a)

# Slicing the array
b= a[3:5]
print(b)

# Set the fourth element and fifth element to 300 and 400
b[3:5] = 300, 400
print(b)

#-----Slicing using [start:end_step]
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5:2])

# If we don't pass start its considered 0
print(arr[:4])

# If we don't pass end it considers till the length of array.
print(arr[4:])

# If we don't pass step its considered 1
print(arr[1:5:])

#----Print the even elements in the given array.
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(arr[1:8:2])




