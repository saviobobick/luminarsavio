m=int(input("Enter first number: "))
n=int(input("Enter second number: "))
t=int(input("Enter third number: "))
if (m>n)&(m>t):
    print(m," is the largest number")
elif(n>m)&(n>t):
    print(n," is the largest number")
else:
    print(t," is the largest number")
