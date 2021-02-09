lst=[10,11,0,12,13,10,9]
ele=int(input("Enter the element to be arranged: "))
for j in lst:
    for i in range(0,len(lst)-1):
        if lst[i]==ele:
            temp=lst[i]
            lst[i]=lst[i+1]
            lst[i+1]=temp
# olist=[]
# for i in lst:
#     if i==ele:
#         olist.append(i)
#         lst.remove(i)
# for i in olist:
#     lst.append(i)
print(lst)
