#To write a NumPy program using methods – info, add, array, all, greater, greater_equal,less, less_equal, equal, allclose, zeroes, ones, linespace, tolist.
#(b) To test whether none of the elements of a given array is zero
import numpy as np
# Create a sample array with no zeros
arr1 = np.array([10, 20, 30, 40, 50])
# Create a sample array with a zero
arr2 = np.array([10, 0, 30, 40, 50])
# Check if none of the elements are zero
is_none_zero_1 = np.all(arr1 != 0)
is_none_zero_2 = np.all(arr2 != 0)
print("Array 1:", arr1)
print("Are none of the elements zero?", is_none_zero_1)
print("\nArray 2:", arr2)
print("Are none of the elements zero?", is_none_zero_2)
