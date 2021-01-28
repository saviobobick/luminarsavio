num1=int(input("enter the frst number"))
num2=int(input("enter the second number"))
num3=int(input("enter the third number"))
if(num1>num2) & (num1>num3):
    if(num2>num3):
        print("num2 is second highest")
    else:
        print("num3 is second highest")
elif(num2>num1)&(num2>num3):
    if(num1>num3):
        print("num1 is second greatest")
    else:
        print("num3 is second greatest")
elif(num3>num1)&(num3>num2):
    if(num2>num1):
        print("num2 is secomnd largest")
    else:
        print("num1 is second largest")
