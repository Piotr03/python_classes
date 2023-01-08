# 1. Compute the multiplication of the following matrices
import numpy as np

a = np.array([[1, 0], [0, 1]])
b = np.array([[1, 2], [3, 4]])

print("a * b = ")
# multiplying a and b
print(a * b)
print()

# 2. Generate an array of length 3n filled with the cyclic pattern 1, 2, 3.
n = 3
print("np.tile([1, 2, 3], 3): ")
# calling the np.tile
print(np.tile([1, 2, 3], n))
print()

# 3. Create a 10×10 matrix of zeros and then "frame" it with a border of ones.
z = np.zeros((10, 10))

# setting the border of z to "1"
z[0, :] = 1
z[-1, :] = 1
z[:, 0] = 1
z[:, -1] = 1
print("10x10 matrix of zeros with border of ones: ")
print(z)
print()

# 4. Create a random 3×5 array using the np.random.rand(3, 5) function and compute:
# the sum of all the entries, the sum of the rows and the sum of the columns.
# (many Numpy functions have an optional axis= argument!)
print("np.random.rand(3, 5) = ")
# storing the random array in r
r = np.random.rand(3, 5)
print(r)
# printing the sum of all the entries
print(r.sum())
# printing the sum of the rows
print(r.sum(axis=0))
# printing the sum of the columns
print(r.sum(axis=1))
print()

# 5. Given the following arrays representing logical values (0 = False, 1 = True) compute the logical
# AND, and logical OR operations for every pair of values of the two arrays: [1, 1, 0, 0] [1, 0, 1, 0]
# Hint: you may need to set the data type (dtype) of the array's elements to 'bool'
c = np.array([1, 1, 0, 0], dtype=bool)
d = np.array([1, 0, 1, 0], dtype=bool)

print("Array 1: ", c)
print("Array 2: ", d)
print("Logical AND: ")
# printing the logical AND
print(np.logical_and(c, d))
print()

print("Logical OR: ")
# printing the logical OR
print(np.logical_or(c, d))
print()

# 6. Find indices of non-zero elements from [1, 2, 0, 0, 4, 0]
e = np.array([1, 2, 0, 0, 4, 0])
print("Indices of non-zero elements in [1, 2, 0, 0, 4, 0]:")
# printing the indices of non-zero elements
print(np.nonzero(e))
print()

# 7. Create a 8×8 array with random values and find minimum and maximum value
f = np.random.rand(8, 8)
print("8x8 array with random values = ")
print(f)
print("Minimum value:", f.min())
print("Maximum value:", f.max())
print()

# 8. Create a 8×8 array with random natural values from the range (1-100) on the diagonal,
# other values should be 0. Hint: You can use numpy's 'eye' function.
g = np.eye(8, 8)
# setting the diagonal of i to random natural values
g = g * np.random.randint(1, 100, (8, 8))
print("8x8 array with random natural values on the diagonal: ")
print(g)
print()


# 9. Write a function which creates an n×n matrix with (i,j)-entry equal to i+j.
def create_matrix(n):
    return np.array([[i + j for i in range(n)] for j in range(n)])


print("n x n matrix with (i,j)-entry equal to i+j = ")
# printing the matrix
print(create_matrix(5))
print()


# 10. Write a function which creates an n×n matrix with rows having subsequent values multiplied by the row's number.
# For example for n = 4:
# [[0, 1, 2, 3], [0, 2, 4, 6], [0, 3, 6, 9], [0, 4, 8, 12]]
def create_matrix2(n):
    row = np.array([i for i in range(n)])
    return np.array([row * (i+1) for i in range(n)])


print("n x n matrix with rows having subsequent values multiplied by the row's number: ")
# printing the matrix
print(create_matrix2(4))