lst=[1,2,3,4,5,6,7,8,9]
evens=list(filter(lambda num:num%2==0,lst))
num=list(filter(lambda num:num>3,lst))
print(evens,num)