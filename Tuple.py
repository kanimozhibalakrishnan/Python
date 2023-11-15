def s1(t):
    res=''
    for i in t:
        res=res+i
    return res

n=int(input("Enter the number of elements in tuple:"))
l=list()
for j in range(0,n):
    e=input("Enter the element")
    l.append(e)
a=tuple(l)
print("The string is",s1(a))
