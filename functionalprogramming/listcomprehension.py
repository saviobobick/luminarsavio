lst1=[1,2,3]
lst2=[3,4,5]
print(list((i,j)for i in lst1 for j in lst2))
print([i**2 for i in lst1])
print([i for i in lst1 if i%2==0])


lst=[3,4,2,6,7,8]
print(list(i-1 if i<5 else i+1 for i in lst))




# lst=[]
# for i in lst1:
#     for j in lst2:
#         lst.append((i,j))
# print(lst)