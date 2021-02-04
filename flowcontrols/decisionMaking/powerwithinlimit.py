p=int(input("Enter the power: "))
n1=int(input("Enter the lower limit: "))
n2=int(input("Enter the upper limit: "))
for i in range(1,n2+1):
    if(i**p>=n1)&(i**p<=n2):
        print(i**p)