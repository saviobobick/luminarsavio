expense={"jan":28000,"feb":30000,"mar":40000,"apr":38000,"may":35000}
print("Expense of february is:",expense["feb"])
expense["apr"]-=2000
expense["june"]=45000
print(expense)
if "mar" in expense:
    print("Entry exist")
else:
    print("Not exist")
for i in expense:
    print(i,expense[i])
