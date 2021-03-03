from re import *
rule="[K][L][0-9]{1,2}[A-Z]{1,2}[0-9]{1,4}"
f=open("regno","r")
for num in f:
    lines=num.rstrip("\n").split(",")
    matches=fullmatch(rule,lines)
lst=[]
for match in matches:
    lst.append(match)
print(lst)