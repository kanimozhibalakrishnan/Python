s1=str(input("Enter the 1st string:"))
s2=str(input("Enter the 2nd string:"))
s3=''
temp=0
ln1=len(s1)
ln2=len(s2)
for i in range(0,ln2):
    for j in range(0,ln1):
        if(s2[i]==s1[j]):
            s3=s3+s1[j]
            temp=j+1
            break

if(s2==s3):
    print('Yes')
else:
    print('No')
