#To write a NumPy program using methods – info, add, array, all, greater, greater_equal,less, less_equal, equal, allclose, zeroes, ones, linespace, tolist.
#(c) To create am element – wise comparison (greater, greater_equal, less, less_equal, equal within a tolerance) of two given arrays.
import numpy as np
# Create two sample arrays
arr1 = np.array([2, 4, 6, 8, 10])
arr2 = np.array([2, 4, 6, 8, 10.000000001])
print("Array 1:", arr1)
print("Array 2:", arr2)
# Element-wise comparisons
print("\nGreater than:", arr1 > arr2)
print("Greater than or equal to:", arr1 >= arr2)
print("Less than:", arr1 < arr2)
