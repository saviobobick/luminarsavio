list=[10,20,30,40,50]
element=int(input("enter the element"))
flag=0
for i in list:
    if(element==i):
        flag=1
        break
    else:
        pass
if(flag==1):
    print("element found")
else:
    print("element not found")
