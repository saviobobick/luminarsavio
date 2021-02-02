l1=int(input("Enter the lower limit: "))
l2=int(input("Enter the upper limit: "))
flag=0
for i in range(l1,l2+1):
    for j in range(2,i):
        if(i%j)==0:
            flag=1
            break
    if flag==0:
        print(i)