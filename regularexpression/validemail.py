from re import *
rule="[\w\d\W]{1,64}@gmail.com"
email=input("Enter your mail id:")
match=fullmatch(rule,email)
if match!=None:
    print("Valid")
else:
    print("Inavlid")