emp={"id":101,"Name":"Anu","Designation":"Software developer","Salary":45000}
print("Name:",emp["Name"],"\n","Designation:",emp["Designation"])
if "Gender" in emp:
    print("Gender exist")
else:
    emp["Gender"]="Female"
print(emp)
for k in emp:
    print(k,emp[k])
