m=int(input("Enter first number: "))
n=int(input("Enter second number: "))
t=int(input("Enter third number: "))
if(m>n)&(m>t):
    if(n>t):
        print(n," is the second largest number")
    else:
        print(t," is the second largest number")
elif(n>t)&(n>m):
    if(t>m):
        print(t," is the second largest number")
    else:
        print(m," is the second largest number")
elif(t>m)&(t>n):
    if(m>n):
        print(m," is the second largest number")
    else:
        print(n," is the second largest number")