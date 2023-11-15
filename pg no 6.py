setx=set(["apple","mango",34,45,75])
sety=set(["mango","orange",34])
setz=set(["mango"])
print("X:",setx)
print("Y:",sety)
print("Z:",setz,"\n")
print("Checking whether X is subset of Y....\n")
if(setx.issubset(sety)==True):
    print("The set X is the subset of Y \n")
else:
    print("The set X is not the subset of Y \n")
print("Checking whether Y is subset of X....\n")
if(sety.issubset(setx)==True):
    print("The set Y is the subset of X \n")
else:
    print("The set Y is not the subset of X \n")
print("Checking whether y is subset of z....\n")
if(sety.issubset(setz)==True):
    print("The set Y is the subset of Z \n")
else:
    print("The set Y is not the subset of Z \n")
print("Checking whether Z is subset of Y....\n")
if(setz.issubset(sety)==True):
    print("The set Zis the subset of Y \n")
else:
    print("The set Z is not the subset of Y \n")
