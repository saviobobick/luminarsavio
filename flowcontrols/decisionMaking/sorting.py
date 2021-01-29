m=int(input("Enter first number: "))
n=int(input("Enter second number: "))
t=int(input("Enter third number: "))
if(m>n)&(m>t):
    if(n>t):
        print(m," ",n," ",t)
    else:
        print(m," ",t," ",n)
elif(n>t)&(n>m):
    if(t>m):
        print(n," ",t," ",m)
    else:
        print(n," ",m," ",t)
elif(t>m)&(t>n):
    if(m>n):
        print(t," ",m," ",n)
    else:
        print(t," ",n," ",m)