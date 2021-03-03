from re import *
rule="[K][L][0-9]{1,2}[A-Z]{1,2}[0-9]{1,4}"
regno=input("Enter your reg number:")
match=fullmatch(rule,regno)
if match!=None:
    print("Valid")
else:
    print("Invalid")
