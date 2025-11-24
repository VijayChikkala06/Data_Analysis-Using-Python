#To write a Python program that demonstrates error handling using try – except block to handle division by zero.
def safe_divide(numerator, denominator):
 """
 Performs division of two numbers, handling ZeroDivisionError.
 Args:
 numerator (float or int): The number to be divided.
 denominator (float or int): The number to divide by.
 Returns:
 float or str: The result of the division, or an error message if division by zero occurs.
 """
 try:
 # Attempt to perform the division
 result = numerator / denominator
 return result
 except ZeroDivisionError:
 # Catch the specific error if division by zero happens
 return "Error: Cannot divide by zero!"
 except TypeError:
 # Catch other potential errors, like dividing non-numeric types
 return "Error: Invalid input. Please enter numbers only."
 except Exception as e:
 # A general catch-all for any other unexpected errors
 return f"An unexpected error occurred: {e}"
# --- Demonstrating the safe_divide function ---
if __name__ == "__main__":
 print("--- Division Error Handling Demonstration ---")
  # Scenario 1: Valid division
 num1 = 12
 den1 = 4
 print(f"\nDividing {num1} by {den1}:")
 division_result1 = safe_divide(num1, den1)
 print(f"Result: {division_result1}")
 # Scenario 2: Division by zero
 num2 = 15
 den2 = 0
 print(f"\nDividing {num2} by {den2}:")
 division_result2 = safe_divide(num2, den2)
 print(f"Result: {division_result2}")
 # Scenario 3: Another valid division
 num3 = 9
 den3 = 3
 print(f"\nDividing {num3} by {den3}:")
 division_result3 = safe_divide(num3, den3)
 print(f"Result: {division_result3}")
 # Scenario 4: Invalid input type (for TypeError demonstration)
 num4 = 20
 den4 = "five"
 print(f"\nDividing {num4} by '{den4}':")
 division_result4 = safe_divide(num4, den4)
 print(f"Result: {
