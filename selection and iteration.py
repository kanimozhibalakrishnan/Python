n=int(input("Enter the number:"))
if n%2==0:
    rev=0
    temp=n
    while(n>0):
        digit=n%10
        rev=rev*10+digit
        n=n//10
    if(rev==temp):
        print("The given number is palindrome")
    else:
        print("The given number is not a palindrome")
else:
    def factorial(n):
        if n==1:
            return n
        else:
            return n*factorial(n-1)
    print("The factorial of",n,"is",factorial(n))
    count=0
    num=factorial(n)
    while(num>0):
        num=num//10
        count=count+1
    print("The number of digit is the factorial of a number is",count)
