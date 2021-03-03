from re import *
rule="(91)?\d{10}"
phno=input("Enter phno:")
match=fullmatch(rule,phno)
if match!=None:
    print("Valid")
else:
    print("Invalid")