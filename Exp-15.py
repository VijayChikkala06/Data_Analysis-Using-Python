#To write a NumPy program using NumPy methods – max, min, argmax, argmin, repr,count, bincount, unique.
#(a) To extract all numbers from a given array which are less and greater than a specific number.
import numpy as np
# Create a sample NumPy array
data = np.array[22 30 35 10 40 28 19 55 25]
# Define the range to filter by
min_val = 20
max_val = 40
print("Original array:", data)
print(f"Filtering for numbers between {min_val} and {max_val}...")
# Use boolean indexing to create a mask for elements in the range
filtered_data = data[(data > min_val) & (data < max_val)]
print("Extracted numbers:", filtered_data)
