# import numpy library
import numpy as np 

# The value of pi
np.pi

# Create the numpy array in radians
x = np.array([0, np.pi/2 , np.pi])

# Calculate the sin of each elements
y = np.sin(x)
print(y)

# LINSPACE -  returns evenly spaced numbers over a specified interval.
# numpy.linspace(start, stop, num = int value)
# num = no. samples to generate

# Makeup a numpy array within [-2, 2] and 5 elements
np.linspace(-2, 2, num=5)

# Make a numpy array within [-2, 2] and 9 elements
np.linspace(-2, 2, num=9)

# Make a numpy array within [0, 2π] and 100 elements 
x = np.linspace(0, 2*np.pi, num=100)

# Calculate the sine of x list
y = np.sin(x)

# Plot the result
plt.plot(x, y)
