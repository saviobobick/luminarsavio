n=int(input("Enter the limit: "))
for i in range(n,0,-1):
    for k in range (i,n+1):
        print(" ",end="")
    for j in range(i,0,-1):
        print("*",end="")
    print()