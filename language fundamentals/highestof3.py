num1=int(input("enter the first number"))
num2=int(input("enter the second number"))
num3=int(input("enter the third number"))
if(num1>num2):
    print("first number is greater than second")
    if(num1>num2):
        print("num1 is greatest of three numbers")
    else:
        print("num3 is greatest of three numbers")

elif(num2>num3):
    print("num2 is greatest of three numbers")
elif(num1==num2==num3):
    print("equal")
else:
    print("num3 is greatest")