lst=[2,6,4,7,8,6]
pos=int(input("Enter pos:"))
try:
    print(lst[pos])
except Exception as e:
    print(e.args)
