# Get input from user
num_terms = int(input("Enter the number of terms to generate: "))

# Initialize variables
n1, n2 = 0, 1
count = 0

# Check if the number of terms is valid
if num_terms <= 0:
   print("Please enter a positive integer")
elif num_terms == 1:
   print("Fibonacci sequence up to", num_terms, ":")
   print(n1)
else:
   print("Fibonacci sequence up to", num_terms, ":")
   while count < num_terms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1
