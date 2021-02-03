limit=int(input("enter the limit"))
lst=[]
sum=0
newlst=[]
for i in range(limit):
    element=int(input("enter element"))
    lst.append(element)
print(lst)
for element in lst:
    sum+=element
print(sum)
for i in lst:
    newlst.append(sum-i)
print(newlst)