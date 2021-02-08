arr=[10,11,12,13,14,15]
ele=int(input("Enter the element to be searched: "))
arr.sort()
# a=sorted(arr)
flag=0
cnt=0
low=0
upp=len(arr)-1
while low<=upp:
    cnt+=1
    mid=(low+upp)//2
    if ele<arr[mid]:
        upp=mid-1
    elif ele>arr[mid]:
        low=mid+1
    elif ele==arr[mid]:
        print("Element found")
        flag=1
        break
if flag==0:
    print("Element not found")
print(cnt)