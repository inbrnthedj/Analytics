# 🐍 Python for Data Science: NumPy Fundamentals

> **Topic**: Numerical Python (1D & 2D Arrays, Vectorization, Indexing, Slicing, and Matrix Operations)

---

## 📌 1. Introduction to NumPy

**NumPy** (short for *Numerical Python*) is the foundational library for scientific computing and data analysis in Python. It provides high-performance multidimensional array objects (`ndarray`) and efficient tools for working with them.

### Why use NumPy instead of Python Lists?

| Feature | Python List | NumPy `ndarray` |
| :--- | :--- | :--- |
| **Data Types** | Dynamic (can mix `int`, `str`, `float`) | Homogeneous (all elements must be same type) |
| **Memory Allocation** | Pointers scattered across memory | Continuous block of memory |
| **Performance** | Slow (requires explicit loops) | Fast (Vectorized C-level execution) |
| **Operations** | Appending, extending, basic slicing | Mathematical & Linear Algebra operations |

### Importing NumPy
Standard convention for importing NumPy:
```python
import numpy as np
```

---

## 🔢 2. NumPy 1D Arrays

A **1-Dimensional array** (vector) is a linear sequence of elements of the same data type.

### Creating 1D Arrays
```python
# Convert a standard Python list to a NumPy array
a = np.array([0, 1, 2, 3, 4])
print(a)  # Output: [0 1 2 3 4]
```

### Essential Array Attributes
```python
a = np.array([10, 20, 30, 40, 50], dtype=np.int64)

# 1. Type of elements
print(a.dtype)   # int64

# 2. Number of elements in array
print(a.size)    # 5

# 3. Number of array dimensions (axes)
print(a.ndim)    # 1

# 4. Tuple indicating shape (size along each dimension)
print(a.shape)   # (5,)
```

### Indexing & Slicing 1D Arrays

- **Positive Indexing**: `a[0]` selects the first element.
- **Negative Indexing**: `a[-1]` selects the last element.
- **Slicing**: Syntax is `array[start:stop:step]` (inclusive of `start`, exclusive of `stop`).

```python
c = np.array([20, 1, 2, 3, 4])

# Indexing
print(c[0])     # 20
print(c[-1])    # 4

# Slicing
print(c[1:4])   # array([1, 2, 3])

# Modifying values using slicing
c[1:4] = [100, 200, 300]
print(c)        # array([ 20, 100, 200, 300,   4])
```

---

## ⚡ 3. 1D Array Operations & Vectorization

NumPy enables **vectorized operations**, eliminating the need to write `for` loops when performing element-wise arithmetic.

### Basic Vector Operations

```python
u = np.array([1, 0])
v = np.array([0, 1])

# 1. Vector Addition
z_add = u + v             # Output: array([1, 1])
# equivalent to: np.add(u, v)

# 2. Vector Subtraction
z_sub = u - v             # Output: array([1, -1])
# equivalent to: np.subtract(u, v)

# 3. Scalar Multiplication
y = 2 * u                 # Output: array([2, 0])

# 4. Element-wise Product (Hadamard Product)
z_mult = u * v            # Output: array([0, 0])

# 5. Dot Product (Scalar Product: u1*v1 + u2*v2)
dot_product = np.dot(u, v) # Output: 0
# Alternative syntax in Python 3.5+: u @ v

# 6. Adding a Scalar (Broadcasting)
u_plus_scalar = u + 1     # Output: array([2, 1])
```

### Universal Functions (`ufuncs`) & Statistical Methods

```python
a = np.array([1, -2, 3, 4, 5])

# Summary Statistics
print(a.mean())   # Mean / Average: 2.2
print(a.std())    # Standard Deviation
print(a.max())    # Maximum value: 5
print(a.min())    # Minimum value: -2

# Universal Functions
print(np.pi)             # Constant pi: 3.141592653589793
x = np.array([0, np.pi/2, np.pi])
y_sin = np.sin(x)        # Element-wise Sine calculation: array([0., 1., 0.])
```

### Linearly Spaced Numbers (`linspace`)
Generates evenly spaced numbers over a specified interval:
```python
# Syntax: np.linspace(start, stop, num)
# Generates 'num' samples from 'start' to 'stop' (inclusive)
x = np.linspace(-2, 2, num=5)
print(x)  # Output: [-2. -1.  0.  1.  2.]
```

---

## 📊 4. NumPy 2D Arrays (Matrices)

A **2-Dimensional array** represents a matrix organized into rows and columns.

### Creating 2D Arrays
```python
# Pass a nested list where each inner list represents a row
A = np.array([[11, 12, 13], 
              [21, 22, 23], 
              [31, 32, 33]])
```

### Attributes of 2D Arrays
```python
print(A.ndim)   # 2 (2 dimensions)
print(A.shape)  # (3, 3) -> 3 rows, 3 columns
print(A.size)   # 9 total elements
```

### Accessing & Slicing 2D Array Elements

```python
# Accessing single element: array[row, column] or array[row][column]
print(A[0, 0])    # 11 (row 0, col 0)
print(A[1, 2])    # 23 (row 1, col 2)

# Slicing Rows & Columns: array[row_slice, col_slice]
# Example: First row, first two columns
print(A[0, 0:2])  # Output: array([11, 12])

# Example: First two rows, last two columns
print(A[0:2, 1:3])
# Output:
# [[12 13]
#  [22 23]]
```

---

## 🧮 5. 2D Array & Matrix Operations

### Matrix Addition & Subtraction
```python
X = np.array([[1, 0], [0, 1]])
Y = np.array([[2, 1], [1, 2]])

Z = X + Y
# Output:
# [[3 1]
#  [1 3]]
```

### Element-wise Multiplication (Hadamard Product)
```python
Z_elem = X * Y
# Output:
# [[2 0]
#  [0 2]]
```

### Matrix Multiplication (Dot Product)
In linear algebra, matrix multiplication requires that the **number of columns in Matrix A equals the number of rows in Matrix B**.

$$\mathbf{C}_{i,j} = \sum_{k} \mathbf{A}_{i,k} \mathbf{B}_{k,j}$$

```python
A = np.array([[0, 1, 1], 
              [1, 0, 1]])  # Shape: (2, 3)

B = np.array([[1, 1], 
              [1, 1], 
              [-1, 1]])    # Shape: (3, 2)

# Matrix multiplication using np.dot or @ operator
C = np.dot(A, B)           # Shape: (2, 2)
# Or: C = A @ B

print(C)
# Output:
# [[0 2]
#  [0 2]]
```

### Matrix Transposition
Swaps rows and columns of a matrix.
```python
A = np.array([[1, 2], [3, 4], [5, 6]])
print(A.shape) # (3, 2)

A_transposed = A.T
# Or: np.transpose(A)

print(A_transposed)
# Output:
# [[1 3 5]
#  [2 4 6]]
print(A_transposed.shape) # (2, 3)
```

---

## 💡 6. Critical Concepts & Useful Helpers

### ⚠️ Views vs. Copies (Memory Management)
* **Slicing creates a View**: Changes to a sliced array **will mutate** the original array!
* **Use `.copy()` for independent arrays**:
```python
a = np.array([1, 2, 3, 4, 5])

# Slice (View)
b = a[0:2]
b[0] = 99
print(a)  # [99, 2, 3, 4, 5] (Original was modified!)

# Copy
c = a[0:2].copy()
c[0] = 1000
print(a)  # [99, 2, 3, 4, 5] (Original unaffected)
```

### Handy Helper Functions

| Function | Description | Example |
| :--- | :--- | :--- |
| `np.zeros(shape)` | Array filled with zeros | `np.zeros((2, 3))` |
| `np.ones(shape)` | Array filled with ones | `np.ones((3, 3))` |
| `np.arange(start, stop, step)` | Array with evenly spaced values | `np.arange(0, 10, 2)` |
| `array.reshape(shape)` | Reshapes array without changing data | `np.arange(6).reshape(2, 3)` |
| `np.eye(N)` | Identity matrix of size N x N | `np.eye(3)` |

---

## 🎯 Summary Checklist
- [x] Know how to define 1D and 2D arrays with `np.array()`.
- [x] Understand array properties: `.dtype`, `.size`, `.ndim`, `.shape`.
- [x] Master indexing & slicing syntax for 1D and 2D arrays.
- [x] Differentiate between Hadamard product (`*`) and Dot product (`np.dot` or `@`).
- [x] Use universal functions (`np.sin`, `a.mean()`, `a.max()`) and `np.linspace()`.
- [x] Understand View vs Copy when slicing arrays.
