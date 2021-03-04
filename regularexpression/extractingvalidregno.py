from re import *
rule="[K][L][0-9]{1,2}[A-Z]{1,2}[0-9]{1,4}"
f=open("regno","r")
lst=[]
for lines in f:
    reg=lines.rstrip("\n")
    match=fullmatch(rule,reg)
    if match!=None:
        lst.append(reg)
print(lst)