# Get input from user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Print the original numbers
print("Before swapping: num1 =", num1, "and num2 =", num2)

# Swap the numbers using a temporary variable
temp = num1
num1 = num2
num2 = temp

# Print the swapped numbers
print("After swapping: num1 =", num1, "and num2 =", num2)
