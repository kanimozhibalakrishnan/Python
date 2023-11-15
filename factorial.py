# Get input from user
num = int(input("Enter a number to find its factorial: "))

# Initialize factorial to 1
factorial = 1

# Calculate factorial
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1, num + 1):
       factorial *= i

   # Print result
   print("The factorial of", num, "is", factorial)
