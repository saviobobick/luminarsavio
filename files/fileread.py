f=open("demo","r")
lst=[]
for lines in f:
    lst.append(lines.rstrip("\n"))
print(lst)