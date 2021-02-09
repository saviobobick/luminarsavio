lst1=[1,2,3,4,5]
lst2=[2,3,10,11,12]
pos1=0
pos2=0
while((pos1<len(lst1))&(pos2<len(lst2))):
    if lst1[pos1]==lst2[pos2]:
        print(lst1[pos1],end=" ")
        pos1+=1
        pos2+=1
    elif lst1[pos1]>lst2[pos2]:
        pos2+=1
    else:
        pos1+=1

# olist=[]
# for i in lst1:
#     for j in lst2:
#         if i==j:
#             olist.append(i)
# print(olist)
