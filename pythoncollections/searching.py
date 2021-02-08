arr=[10,11,12,13,14,15]
ele=int(input("Enter the element to be searched: "))
flag=0
cnt=0
for num in arr:
    cnt+=1
    if ele==num:
        flag=1
        break
if flag==1:
    print("Element found")
else:
    print("Element not found")
print(cnt)