num=int(input("Enter the number: "))
flag=0
for i in range(20,51):
    if num==i:
        print("True")
        flag=1
        break
if flag==0:
    print("False")

# if num in range(20,50):
#     print("True")
# else:
#     print("False")