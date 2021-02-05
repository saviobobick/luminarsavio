lst=[4,9,2]
s=0
olist=[]
for num in lst:
    s+=num
for num in lst:
    num=s-num
    olist.append(num)
print(olist)


