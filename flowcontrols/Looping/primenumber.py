num=int(input("Enter a number: "))
if num<1:
    print("Error")
else:
    t=0
    for i in range(2,num):
        if (num%i)==0:
            t=1
    if t==0:
        print("Number is prime")
    else:
        print("Number is not prime")