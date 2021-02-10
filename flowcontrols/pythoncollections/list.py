list1=[10,20,30,40]
list2=[20,40,60,80]
pos1=0
pos2=0
length1=len(list1)
length2=len(list2)
while(pos1<length1) & (pos2<length2):
    if list1[pos1]==list2[pos2]:
        print(list1[pos1])
        pos1+=1
        pos2+=1
    elif list1[pos1]>list2[pos2]:
        pos2+=1
    else:
        pos1+=1
