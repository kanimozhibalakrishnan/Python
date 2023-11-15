a=int(input("Enter the 1st number:"))
b=int(input("Enter the 2nd number:"))
c=int(input("Enter the 3rd number:"))

if (a>=b) and (a>=c):
    largest=a
elif (b>=a) and (b>=c):
    largest=b
elif (c>=a)and(c>=b):
    largest=c
else:
    print("Enter a positive value")

    print("The largest of three numbers is",largest)
