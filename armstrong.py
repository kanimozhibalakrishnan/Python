# Get input from user
num = int(input("Enter a number to check if it's an Armstrong number: "))

# Initialize variables
sum = 0
order = len(str(num))

# Calculate sum of cubes of digits
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** order
   temp //= 10

# Check if the number is an Armstrong number
if num == sum:
   print(num, "is an Armstrong number")
else:
   print(num, "is not an Armstrong number")
