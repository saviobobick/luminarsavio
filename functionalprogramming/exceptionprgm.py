num1=int(input("Enter num1:"))
num2=int(input("Enter num2:"))
try:
    if num2<0:
        raise Exception("invalid")
    res=num1/num2
    print(res)
except Exception as e:
    print(e.args)
finally:
    print("done")

