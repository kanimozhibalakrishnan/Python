n=int(input("Enter no.of elements in list:"))
l=list()
for i in range(0,n):
    e=input("Enter the element of list")
    l.append(e)
print("Original list"+str(l))

flag=0
'''i=1
while i<len(l):
    if(l[i]<l[i-1]):
        flag=1
    i+=1'''
l1=l[:]
l1.sort()
if(l1==l):
    flag=1

'''if(not flag):
    print("Yes the list is in ascending order.")
else:
    print("No the list is not in ascending order.")'''

if(flag):
    print("Yes the list is in ascending order.")
else:
    print("No the list is not in ascending order.")
