lst=[2,3,4,5]
num=int(input("Enter a number: "))
# for i in lst:
#     for j in lst:
#         if (i+j==num)&(i!=j):
#             print(i,j)
#             break
low=0
upp=len(lst)-1
flg=0
while(low<upp):
    if(lst[low]+lst[upp]==num):
        print(lst[low],lst[upp])
        flg=1
        low+=1
        upp-=1
    elif(lst[low]+lst[upp]<num):
        low+=1
    else:
        upp-=1
if flg==0:
    print("No pair")